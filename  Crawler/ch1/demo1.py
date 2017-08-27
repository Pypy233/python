from urllib.request import urlopen
html = urlopen("http://www.baidu.com/pages/page1.html")
print(html.read())