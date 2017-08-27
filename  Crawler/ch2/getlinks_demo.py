from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random
import ssl
random.seed(datetime.datetime.now())
def getLinks(url):
	context = ssl._create_unverified_context()
	html = urlopen("http://en.wikipedia.org" + url, context = context)
	bsObj = BeautifulSoup(html, 'html5lib')
	return bsObj.find("div", {"id":"bodyContent"}).findAll("a", href=re.compile("^(/wiki/)((?!:).)*$"))

links = getLinks("/wiki/Kevin_Bacon")
while(len(links) > 0):
	newArticle = links[random.randint(0, len(links) - 1)].attrs('href')
	print(newArticle)