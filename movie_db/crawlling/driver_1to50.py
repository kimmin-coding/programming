from bs4 import BeautifulSoup as bs
import requests,re,os
from urllib.request import urlretrieve
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys


driver=webdriver.Chrome('chromedriver.exe')
driver.get("https://zzzscore.com/1to50/")

driver.implicitly_wait(300)

btns = driver.find_elements_by_xpath('//*[@id="grid"]/div[*]')
print(btns)



temp={}
for val,k in enumerate(btns):
    temp[k.text]=val

print(temp)



for i in range(1,26):
    btns[temp[str(i)]].click()

        # for btn in btns:
        #     if btn.text==str(val):
        #         print(btn.text)
        #         btn.click() 

time.sleep(0.5) 
temp={}
for val,k in enumerate(btns):
    temp[k.text]=val


 
print(temp)

for i in range(26,51):
    btns[temp[str(i)]].click()
time.sleep(5)
driver.quit()





try:
    if not (os.path.isdir("image")):
        os.makedirs(os.path.join("image"))
except OSError as e:
    if e.errno != errno.EXIST:
        print("폴더가 생성되지 않았습니다.")
        exit()

#//*[@id="search"]

html=requests.get("https://comic.naver.com/webtoon/weekday")

soup=bs(html.text,'html.parser')
html.close()

data1=soup.findAll('div',{"class":"col_inner"})
# title=data1[1].findAll("a",{"class":"title"})

t_list=[]

for t in data1:
    
    t_list.extend(t.findAll("li"))

for li in t_list:
    img=li.find("img")
    title=img["title"]
    img_src=img["src"]
    title=re.sub("[^0-9a-zA-Zㄱ_힗]", '',title)
    urlretrieve(img_src, './image/'+title+".jpg")

print("Download complete")