import sqlite3
import sys
from PyQt5 import QtWidgets
from PyQt5 import uic


db=__file__.replace("report.py","book_report.db")
class Form(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self,parent)
        
        self.ui = uic.loadUi(__file__.replace(".py",".ui"), self)
        
        self.ui.show()
        print(__file__)

    def first(self):
        conn=sqlite3.connect(db)
        cur=conn.cursor()

        strQuery="select * from report"

        cur.execute(strQuery)
        records=cur.fetchall()
        
        # self.tableWidget.setRowCount(len(records))
        # self.tableWidget.setColumnCount(0)
        # for row , rowval in enumerate(records):
        #     for col,cell in enumerate(rowval):
        #         self.tableWidget.setItem(row, col, QtWidgets.QTableWidgetItem(cell))

    def search(self):
        pass          
if __name__=="__main__" :
    app = QtWidgets.QApplication(sys.argv)
    w= Form()
    sys.exit(app.exec())