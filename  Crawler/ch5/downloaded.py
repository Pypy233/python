import os
from urllib.request import urlopen
from urllib.request import urlretrieve
from bs4 import BeautifulSoup

downloadDirectory = 'download'
baseUrl = 'http://pythonscraping.com'

def getAbosulateUrl(baseUrl, source):
	if source.startwith('http://www.'):
		url = 'http://' + source[11:]
	elif source.startwith('http://'):
		url = source
	elif source.startwith('www.'):
		url = 'http://' + source[4:]
	else:
		url = baseUrl + '/' + source
	if baseUrl not in url:
		return None
	return url


