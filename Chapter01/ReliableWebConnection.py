from urllib.request import urlopen

try:
    html = urlopen("http://pythonscraping.com/pages/page1.html")
    print(html.read())
except HttpError as e:
    print(e)