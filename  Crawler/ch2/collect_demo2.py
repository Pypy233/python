from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import ssl
context = ssl._create_unverified_context()
html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon', context = context)
bsObj = BeautifulSoup(html, 'html5lib')
for link in bsObj.find('div', {"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$")):
	if 'href' in link.attrs:
		print(link.attrs['href'])