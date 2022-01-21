import sys
from PyQt5 import QtWidgets
from PyQt5 import uic
import json 

class Form(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self,parent)
        
        ui=__file__.split('\\')[-1].split('.')[0]+".ui"
        self.ui = uic.loadUi(ui, self)
        print(__file__)
        
        self.ui.show()

    def login(self):
        id=self.id_lineEdit.text()
        pw=self.pw_lineEdit.text()

        
        #파일 만들기
        f=open("test_file","r")
        

        temp=f.readline() 
        temp=dict(json.loads(temp))
        temp_id=list(temp.keys())
        temp_pw=list(temp.values())
        
        
        if id in temp_id:
            if pw==temp[id]:
                print("로그인 성공")

            else:
                print("로그인 실패")
        else:
            print("로그인 실패")
        # if id==temp[0][3:-1] and pw==temp[1][3:]:
        #     print("로그인 성공")
        
        # else:
        #     print("로그인 실패")

        f.close()

        #레이블값 가져오기
        #self.label.text()

        #레이블 출력
        #self.label.setText('12334')

       # print(self.pushButton.text())
        # self.chcolor()

    def signup(self):
        print("signup")
        

    def chcolor(self):
        self.pushButton.setText('Login')
        #print(self.pushButton.())

if __name__=="__main__" :
    app = QtWidgets.QApplication(sys.argv)
    w= Form()
    sys.exit(app.exec())