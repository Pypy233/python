from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import ssl
pages = set()
def getLinks(pageUrl):
	global pages
	global count
	count = 0
	context = ssl._create_unverified_context()
	html = urlopen('http://en.wikipedia.org' + pageUrl, context = context)
	bsObj = BeautifulSoup(html, 'html5lib')
	for link in bsObj.findAll('a', href = re.compile('^(/wiki/)')):
		if 'href' in link.attrs:
			if link['href'] not in pages and count <= 20:
				newPage = link['href']
				print(newPage)
				count += 1
				pages.add(newPage)
				getLinks(newPage)
def main():
	getLinks('')

main()