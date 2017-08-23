from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bsObj = BeautifulSoup(html, 'html5lib')
for child in bsObj.find('table', {'id':'giftList'}).children:
	print(child)
print('*************')
for sibing in bsObj.find('table', {'id':'giftList'}).tr.children:
	print(sibing)