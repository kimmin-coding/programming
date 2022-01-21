import sqlite3
import sys
from PyQt5 import QtWidgets
from PyQt5 import uic

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

        strQuery="select * from keep_book "

        cur.execute(strQuery)
        records=cur.fetchall()
        
        self.tableWidget.setRowCount(len(records))
        self.tableWidget.setColumnCount(5)
        for row , rowval in enumerate(records):
            for col,cell in enumerate(rowval):
                if col==3 or col==4:
                    cell=str(cell)
                self.tableWidget.setItem(row, col, QtWidgets.QTableWidgetItem(cell))        


        cur.close()
        conn.close()
        
        



    def quit(self):
        exit()

    def pict(self):
        pass


if __name__=="__main__" :
    app = QtWidgets.QApplication(sys.argv)
    w= Form()
    sys.exit(app.exec())