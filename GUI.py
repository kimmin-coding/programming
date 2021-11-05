import sys
from PyQt5 import QtWidgets
from PyQt5 import uic

class Form(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self,parent)
        
        ui=__file__.split('\\')[-1].split('.')[0]+".ui"
        self.ui = uic.loadUi(ui, self)
        print(__file__)
        
        self.ui.show()
    def test(self):
        print("test")
        self.chcolor()

    def chcolor(self):
        self.pushButton.setStyleSheet('QPushButton {background-color: #000000; color: red;}')
        self.pushButton.setText('Press me')
        print(self.pushButton.getText())

if __name__=="__main__" :
    app = QtWidgets.QApplication(sys.argv)
    w= Form()
    sys.exit(app.exec())