from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

# 
def getColoredText(bsObj,color):
    nameList = bsObj.findAll("span",{"class": color})
    for name in nameList:
        print(name.text)

def myTestFunc(url):
    with urlopen(url) as html:
        bsObj = BeautifulSoup(html,"html.parser")
        getColoredText(bsObj,"green")

myTestFunc("http://www.pythonscraping.com/pages/warandpeace.html")