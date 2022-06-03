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
from selenium.webdriver.common.by import By
#브라우저 띄우지 않기----스크롤 아래는 안띄워져 오류 ∴보류
# chrome_options = webdriver.ChromeOptions()                          
# chrome_options.add_argument('headless')
# driver=webdriver.Chrome('chromedriver.exe',chrome_options=chrome_options)



class Form(QtWidgets.QMainWindow):
    
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self,parent)
        
        self.ui =uic.loadUi(__file__.replace(".py",".ui"), self)
        self.ui.show()

        # driver.get("https://namu.wiki/w/냥코%20대전쟁/스테이지/세계편")
        

    def selected(self):
        driver=webdriver.Chrome('chromedriver.exe')
        driver.get("https://namu.wiki/w/냥코%20대전쟁/스테이지/세계편")
        
       
        # btns = driver.find_element_by_xpath('//*[@id="UH8UomIFA"]/article/div[7]/div/div/div/div/div/div/div/div[4]/div/div/div/div/div/div/div[2]/div[1]/div/div[10]')
        # txt=driver.find_element_by_xpath('//*[@id="UH8UomIFA"]/article/div[7]/div/div/div/div/div/div/div/div[4]/div/div/div/div/div/div/div[2]/div[1]/div/div[10]')
        # txt=driver.find_element_by_id('스테이지 11~20')


        #Todo; 스테이지 48일때 h4로 나눠서 해당 장으로 이동하기
        if self.comboBox_1.currentText()=="스테이지 48":
            pass
            txt=driver.find_element_by_xpath('//*[@id="'+self.comboBox_1.currentText()+'"]/ancestor::h3[1]/following-sibling::div[1]').find_elements_by_tag_name("ul")
            note=driver.find_element_by_xpath('//*[@id="'+self.comboBox_1.currentText()+'"]/ancestor::h3[1]/following-sibling::div[1]').find_elements_by_tag_name("a")

        else:
            txt=driver.find_element_by_xpath('//*[@id="'+self.comboBox_1.currentText()+'"]/ancestor::h3[1]/following-sibling::div[1]').find_elements_by_tag_name("ul")
            note=driver.find_element_by_xpath('//*[@id="'+self.comboBox_1.currentText()+'"]/ancestor::h3[1]/following-sibling::div[1]').find_elements_by_tag_name("a")
        note_list=[]
        temp=''
        for t in txt:
            temp += t.text +"\n\n"
        
        for n in note:
            n=n.text            
            if "[" in n:
                temp=temp.replace(n,'')
        print(temp)

        self.textEdit.setText(temp)
        driver.quit()
                




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