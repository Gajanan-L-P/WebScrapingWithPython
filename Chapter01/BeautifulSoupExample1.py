from urllib.request import urlopen
from bs4 import BeautifulSoup
# html = urlopen("http://www.pythonscraping.com/pages/page1.html")
# bsObj = BeautifulSoup(html.read())
# print(bsObj.h1)

with urlopen("http://www.pythonscraping.com/pages/page1.html") as html:
    # print(html.read())
    bsObj = BeautifulSoup(html.read(),features="html.parser")
    print(bsObj.h1)