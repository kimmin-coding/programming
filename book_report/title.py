import sqlite3
import sys
from PyQt5 import QtWidgets
from PyQt5 import uic
import home

class Form(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self,parent)
        
        self.ui = uic.loadUi(__file__.replace(".py",".ui"), self)
        
        self.ui.show()
        print(__file__)

    def show2(self):
        home.Form().show()
        self.close()
          
if __name__=="__main__" :
    app = QtWidgets.QApplication(sys.argv)
    w= Form()
    sys.exit(app.exec())