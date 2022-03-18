import sqlite3
import sys
import book
from PyQt5 import QtWidgets
from PyQt5.QtCore import QDate
from PyQt5 import uic
import report
import urllib.request

db=__file__.replace("home.py","book_report.db")

class Form(QtWidgets.QDialog):
    
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self,parent)
        
        self.ui = uic.loadUi(__file__.replace(".py",".ui"), self)
        self.first()
        self.ui.show()
    
    def first(self):
        conn=sqlite3.connect(db)
        cur=conn.cursor()

        strQuery="select distinct * from keep_book"

        cur.execute(strQuery)
        records=cur.fetchall()
        
        self.tableWidget.setRowCount(len(records))
        
        self.tableWidget.setColumnCount(6)
        for row , rowval in enumerate(records):
            for col,cell in enumerate(rowval):
                
                self.tableWidget.setItem(row, col, QtWidgets.QTableWidgetItem(cell))
                


        cur.close()
        conn.close()
        self.tableWidget.setHorizontalHeaderLabels(["date", "ISBN","title","publisher","author","memo"])
        #print(QDate.currentDate())
        self.date_wid.setDate(QDate.currentDate())
        #print(str(self.date_wid.date().toPyDate()))
      

        
        

    def quit(self):
        exit()
    
    def delete(self):
        reply = QtWidgets.QMessageBox.question(self, 'Warning', 'Are you sure to quit? If you delete, you cannot get it back.',
                                    QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)
        if reply==QtWidgets.QMessageBox.Yes:
            currow=self.tableWidget.currentRow()
                
            
            if currow>-1:
                date=self.tableWidget.item(currow,0).text()
                ISBN=self.tableWidget.item(currow,1).text()
                


                conn=sqlite3.connect(db)
                cur=conn.cursor()
                
                #print(date,ISBN)
                strQuery="delete from keep_book WHERE date= '"+date.replace("'","''")+"' and ISBN= '"+ISBN.replace("'","''")+"'"
                
                cur.execute(strQuery)
                conn.commit()

                cur.close()
                conn.close()
                self.first()
            else:
                reply = QtWidgets.QMessageBox.question(self, 'Warning', 'Please choose item',
                                    QtWidgets.QMessageBox.Yes)

    def report(self):
        report.Form().first()


    def add(self):
        conn=sqlite3.connect(db)
        cur=conn.cursor()
        #print(book.chk_ISBN("9788997924271"))
        currow=self.tableWidget.currentRow()


        date=self.tableWidget.item(currow,0).text()
        ISBN=self.tableWidget.item(currow,1).text()

        t=self.t_line.text().replace("'","''")
        d=self.date_wid.text().replace("'","''")
        p=self.p_line.text().replace("'","''")
        a=self.a_line.text().replace("'","''")
        I=self.I_line.text().replace("'","''")
        
        m=self.m_Text.toPlainText().replace("'","''")
        print(m)
        #print(d,I,date,ISBN)
        strQuery="select count(ISBN) from keep_book"
        strQuery+=' where ISBN="'+I+'" and date="'+d+'"'
        cur.execute(strQuery)
        records=cur.fetchall()

        # print(strQuery)
        # print(records[0][0])
        if records[0][0]==0:

            
            strQuery="INSERT INTO keep_book "
            strQuery+=" VALUES('"+d+"' , '"+I+"' "
            strQuery+=",'"+t+"','"+p+"','"+I+"',"+m+");"
        else:
            strQuery="update keep_book set date ='"+d+"', ISBN = '"+I+"', title= '"+t+"', publisher='"+p+"', author='"+a+"', memo='"+m+"'"
            strQuery+="where date='"+date+"' and ISBN='"+ISBN+"'"


            
        print(strQuery)
        
        cur.execute(strQuery)
        conn.commit()

        cur.close()
        conn.close()
        self.first()


    def selected(self):
        currow=self.tableWidget.currentRow()
        #print(self.tableWidget.item(currow,0).text())
        a,b,c=map(int,self.tableWidget.item(currow,0).text().split("-"))
        #print(a,b,c)
        self.date_wid.setDate(QDate(a,b,c))
        self.I_line.setText(self.tableWidget.item(currow,1).text())
        self.t_line.setText(self.tableWidget.item(currow,2).text())
        self.p_line.setText(self.tableWidget.item(currow,3).text())
        self.a_line.setText(self.tableWidget.item(currow,4).text())
        self.m_Text.setText(self.tableWidget.item(currow,5).text())

    
        
    def clear(self):
        self.date_wid.setDate(QDate.currentDate())
        self.I_line.clear()
        self.t_line.clear()
        self.p_line.clear()
        self.a_line.clear()
        self.m_Text.clear()

        
    
if __name__=="__main__" :
    app = QtWidgets.QApplication(sys.argv)
    w= Form()
    sys.exit(app.exec())

