from urllib.request import urlopen
html = urlopen("http://pythonscraping.com.pages.pages1.html")
print(html.read())