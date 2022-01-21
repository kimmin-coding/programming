import sys
from PyQt5 import QtWidgets
from PyQt5 import uic
#import json 

class Form(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self,parent)
        
        ui=__file__.split('\\')[-1].split('.')[0]+".ui"
        self.ui = uic.loadUi(ui, self)
        print(__file__)
        
        self.ui.show()

    def save(self):
        # print(self.ed_name.text())
        # print(self.ed_birth.text())
        # print(self.ed_school.text())
        # print(self.ed_grade.text())
        print(self.date_birth.date().toString("yyyy-MM-dd"))
        l=[]
        f=open("student_info.csv","a")
        l.append(self.ed_name.text())
        # l.append(self.date_birth.setDisplayFormat(str))
        l.append(self.ed_school.text())
        l.append(self.ed_grade.text())
        l.append(self.ed_address.text())
        # print(l)
        f.write(",".join(l)+"\n")
        f.close()

    def load(self):
        f= open("student_info.csv","r")
        a=f.read()
        self.textEdit.setText(a)
        f.close()

if __name__=="__main__" :
    app = QtWidgets.QApplication(sys.argv)
    w= Form()
    sys.exit(app.exec())