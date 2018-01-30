from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
context = ssl._create_unverified_context()
html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon', context = context)
bsObj = BeautifulSoup(html, 'html5lib')
for link in bsObj.findAll('a'):
	if 'href' in link.attrs:
		print(link['href'])
