import sqlite3
import sys
from PyQt5 import QtWidgets
from PyQt5 import uic
import report

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
        
        self.tableWidget.setColumnCount(5)
        for row , rowval in enumerate(records):
            for col,cell in enumerate(rowval):
                
                self.tableWidget.setItem(row, col, QtWidgets.QTableWidgetItem(cell))
                


        cur.close()
        conn.close()
        self.tableWidget.setHorizontalHeaderLabels(["date", "ISBN","title","publisher","author"])
        

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
                
                print(date,ISBN)
                strQuery="delete from keep_book WHERE date= '"+date.replace("'","''")+"' and ISBN= '"+ISBN.replace("'","''")+"'"
                print(strQuery)
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


        t=self.t_line.text().replace("'","''")
        d=self.d_line.text().replace("'","''")
        p=self.p_line.text().replace("'","''")
        a=self.a_line.text().replace("'","''")
        I=self.I_line.text().replace("'","''")
    
        strQuery="INSERT INTO keep_book "
        strQuery+=" VALUES('"+d+"' , '"+I+"' "
        strQuery+=",'"+t+"','"+p+"','"+I+"');"



        
        cur.execute(strQuery)
        conn.commit()

        cur.close()
        conn.close()
        self.first()


    def selected(self):
        currow=self.tableWidget.currentRow()
        self.d_line.setText(self.tableWidget.item(currow,0).text())
        self.I_line.setText(self.tableWidget.item(currow,1).text())
        self.t_line.setText(self.tableWidget.item(currow,2).text())
        self.p_line.setText(self.tableWidget.item(currow,3).text())
        self.a_line.setText(self.tableWidget.item(currow,4).text())

    
        
        


if __name__=="__main__" :
    app = QtWidgets.QApplication(sys.argv)
    w= Form()
    sys.exit(app.exec())