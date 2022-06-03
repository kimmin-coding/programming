from bs4 import BeautifulSoup as bs
import requests,re,os
from urllib.request import urlretrieve
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


driver=webdriver.Chrome('chromedriver.exe')
driver.get("https://zzzscore.com/color/")

driver.implicitly_wait(50)
t=time.time()

while t-time.time()<=60:
    btns=driver.find_element_by_class_name("main")
    
    # btns = driver.find_elements_by_xpath('//*[@id="grid"]/div')
    # rgba= [btn.value_of_css_property("background-color") for btn in btns]

    # # print(rgba)


    # print("___________________")

    # dic={}
    # for btn in btns:
    #     if btn.value_of_css_property("background-color") in dic:
    #         dic[btn.value_of_css_property("background-color")]+=1
    #     else:
    #         dic[btn.value_of_css_property("background-color")]=1


    # # print(sorted(dic.items(),key=lambda x:x[1]))
    # answer=sorted(dic.items(),key=lambda x:x[1])[0][0]
    # # print(answer)
    # index=rgba.index(answer)

    # print(index)
    btns.click()
    time.sleep(0.3)

print("done")





# brns_rgb=[btn.value_]
# for k,val in enumerate(btns):
    # print(k,val)



# temp={}
# for val,k in enumerate(btns):
#     temp[k.text]=val

# print(temp)



# for i in range(1,26):
#     btns[temp[str(i)]].click()

        # for btn in btns:
        #     if btn.text==str(val):
        #         print(btn.text)
        #         btn.click() 

# time.sleep(0.5) 
# temp={}
# for val,k in enumerate(btns):
#     temp[k.text]=val


 
# print(temp)

# for i in range(26,51):
#     btns[temp[str(i)]].click()
# time.sleep(5)
# driver.quit()
