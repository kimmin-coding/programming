# import encodings
# import requests
from urllib import parse
from bs4 import BeautifulSoup
from urllib.request import urlopen





C_name=input("나라 이름")
html=urlopen("https://search.naver.com/search.naver?query="+parse.quote(C_name))
bs0bj = BeautifulSoup(html,"html.parser")

print(str(bs0bj.find("span",{"class":"over_text overtext_maxwidth"})).split("<a href=")[0].split(">")[1])
# for child in bs0bj.find("img",{"src":"..img/gifts/img1.jpg"}).parent.previous_sibling.get_text():
#     print(child)





# url불러오기
# session=requests.session()
# url_bookpage="https://search.kyobobook.co.kr/web/search?vPstrKeyWord=9791164500352"
# res=session.get(url_bookpage)
# res.raise_for_status()

#파일에 저장
# soup=BeautifulSoup(res.text, "html.parser")
# f=open("result.txt","w",encoding="utf-8")
# print("",file=f)

#원하는 값 가져오기
# price=soup.findAll("div",{"class":"author"})
# # print(type(price))
# price=price.findAll("a")
# print(price)

#id,pw설정
# login_id="plantrevol2@gmail.com"
# password="kims7464"

#로그인하기
# login_info={
    # "login_id":login_id,
#     "password":password
# }
# url_login="www.acmicpc.net/signin"
# res=session.post(url_login,data=login_info)
# res.raise_for_status()

# print(res.text)