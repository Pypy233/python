from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bsObj = BeautifulSoup(html, 'html5lib')
for child in bsObj.find('table', {'id':'giftList'}).children:
	print(child)
print('*************')
for sibling in bsObj.find('table', {'id':'giftList'}).tr.next_siblings:
	print(sibling)
print('*************')
for sibling in bsObj.find('table', {'id':'giftList'}).tr.previous_siblings:
	print(sibling)
print('*************')