from msilib import Table
from msilib.schema import tables
import sqlite3
import sys
from PyQt5 import QtWidgets
from PyQt5 import uic

db=__file__.replace("select_table_view.py","movie.db") 

class Form(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self,parent)
        
        self.ui = uic.loadUi(__file__.replace(".py",".ui"), self)
        self.select_m()
        self.ui.show()
        

    def select_m(self):    

        conn=sqlite3.connect(db)
        cur=conn.cursor()

        strQuery="select * from movie_watch "
        search_title=self.search_tb.text()

        if len(search_title)>0:
            strQuery+=" where title like'%"+search_title+"%'"
        strQuery+=" ORDER BY key"

        cur.execute(strQuery)
                
        records=cur.fetchall()
        
        self.tableWidget.setRowCount(len(records))
        self.tableWidget.setColumnCount(5)
        for row , rowval in enumerate(records):
            for col,cell in enumerate(rowval):
                if col==3 or col==4:
                    cell=str(cell)
                self.tableWidget.setItem(row, col, QtWidgets.QTableWidgetItem(cell))     
    
        self.tableWidget.setHorizontalHeaderLabels(["date", "title","theater","score","key"])

        # self.tableWidget.setRowCount(2)
        # self.tableWidget.setColumnCount(2)
        # self.tableWidget.setItem(0, 0, QtWidgets.QTableWidgetItem("(0,0)"))
        # self.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem("(0,1)"))
        # self.tableWidget.setItem(1, 0, QtWidgets.QTableWidgetItem("(1,0)"))
        # self.tableWidget.setItem(1, 1, QtWidgets.QTableWidgetItem("(1,1)"))




        cur.close()
        conn.close()
     
    def delete(self):
        reply = QtWidgets.QMessageBox.question(self, 'Message', 'Are you sure to quit?',
                                    QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        if reply==QtWidgets.QMessageBox.Yes:


            currow=self.tableWidget.currentRow()   #선택한 row값 가져오기
            if currow>-1:
                key=self.tableWidget.item(currow,4).text()     #key값 가져오기

                conn=sqlite3.connect(db)
                cur=conn.cursor()

                strQuery="delete from movie_watch where key="+key

                cur.execute(strQuery)
                conn.commit()

                cur.close()
                conn.close()

                self.select_m()
    
    def save(self):
        currow=self.tableWidget.currentRow()   #선택한 row값 가져오기
        
        if currow>-1:
            
            m_date=self.tableWidget.item(currow,0).text()
            m_title=self.tableWidget.item(currow,1).text()
            m_theater=self.tableWidget.item(currow,2).text()
            m_score=self.tableWidget.item(currow,3).text()
            

            if self.tableWidget.item(currow,4)!=None:
                m_k=self.tableWidget.item(currow,4).text()
                conn=sqlite3.connect(db)
                cur=conn.cursor()

                strQuery="update movie_watch "
                strQuery+=" set date='"+m_date+"',title='"+m_title+"',theater='"+m_theater+"', score="+m_score+" "
                strQuery+=" where key="+m_k
            
            else:

                conn=sqlite3.connect(db)
                cur=conn.cursor()

                strQuery="insert into movie_watch(date,title,theater,score) "
                strQuery+=" values('"+m_date+"','"+m_title+"','"+m_theater+"',"+m_score+" )"
                

            cur.execute(strQuery)
            conn.commit()
        


            cur.close()
            conn.close()

            self.select_m()

    def add(self):
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)

    def search(self):
        pass
    #     conn=sqlite3.connect("movie.db")
    #     cur=conn.cursor()

    #     strQuery="select title from movie_watch"
    #     print(strQuery)
    #     cur.execute(strQuery)

                
    #     records=cur.fetchall()
    
        

        

if __name__=="__main__" :
    app = QtWidgets.QApplication(sys.argv)
    w= Form()
    sys.exit(app.exec())