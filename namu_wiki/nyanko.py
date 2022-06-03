from msilib.schema import ComboBox
from tkinter.ttk import Combobox
from bs4 import BeautifulSoup as bs
import requests,re,os
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from PyQt5 import uic
import sqlite3
import sys
from PyQt5 import QtWidgets
import urllib.request


print(sys.path)
sys.path.append(os.path.dirname(os.path.dirname(__file__)))




class Form(QtWidgets.QMainWindow):
    
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self,parent)
        
        self.ui =uic.loadUi(__file__.replace(".py",".ui"), self)
        self.ui.show()



    def selected(self):
        print(self.tabWidget.World)
        # if self.currentText()=="1st~10th":
            # print(1)
        

if __name__=="__main__" :
    app = QtWidgets.QApplication(sys.argv)
    w= Form()
    sys.exit(app.exec())







# if "편" not in a:
#     driver.get("https://namu.wiki/w/냥코%20대전쟁/스테이지/"+a)

# # elif a==
# time.sleep(3)    



# a=input("검색")
# if a=="스테이지":
#     driver.find_element_by_class_name("DWU5pZeZ").click()