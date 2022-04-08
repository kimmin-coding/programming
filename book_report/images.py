import sqlite3
import sys
from PyQt5 import QtWidgets
from PyQt5 import uic
import home
from PyQt5.QtGui import QPixmap
import os



db=__file__.replace("images.py","image.db")
RS_Path=os.path.dirname(__file__)+"\\resource"   #resource 경로
# print(RS_Path)
class Form(QtWidgets.QDialog):
    def first(self):
        conn=sqlite3.connect(db)
        cur=conn.cursor()
        strQuery="select * from images"
        cur.execute(strQuery)
        self.label.setPixmap(QPixmap(RS_Path+"\\image.png"))   #이미지 파일 불러오기


        cur.close()
        conn.close()

        # print(__file__)

    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self,parent)
        
        self.ui = uic.loadUi(__file__.replace("images.py","image.ui"), self)
        self.first()
        self.ui.show()
        

    

    def image():
        pass
          
if __name__=="__main__" :
    app = QtWidgets.QApplication(sys.argv)
    w= Form()
    sys.exit(app.exec())