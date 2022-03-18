import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

req="https://book.naver.com/search/search.naver"
values={
    'isbn':"9788965023128"
}
params=urllib.parse.urlencode(values)    

url=req+"?query="+params
print("url=",url)
data=urllib.request.urlopen(url).read()
text=data.decode("utf-8")

soup=BeautifulSoup(text,'html.parser')
# print(soup.find_all("a"))

print(soup.select('#searchBiblioList'))
# print (soup.html.body.a)

# print(text)

# //*[@id="searchBiblioList"]/li/dl/dt/a
# print(req)

# f=open("result.txt","w")
# print(req.read().decode("utf-8"),file=f)