from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/page1.html")
bsObj = BeautifulSoup(html.read(), "html5lib")
print(bsObj.h1)
'''It seems that I need the html.parser to get rid of the warning.'''