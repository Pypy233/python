from urllib.request import urlopen
from urllib.request import urlretrieve
from bs4 import BeautifulSoup
html = urlopen('http://www.pythonscraping.com')
bsObj = BeautifulSoup(html, 'html5lib')
imageLocation = bsObj.find('a', {'id': 'logo'}).find('img')['src']
urlretrieve(imageLocation, 'logo.jpg')
