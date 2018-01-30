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
def getDownloadPath(baseUrl, absoluteUrl, downloadDirectory):
	path = absoluteUrl.replace('www.', '')
	path = path.replace(baseUrl, '')
	path = downloadDirectory + path
	directory = os.path.dirname(path)
	if not os.path.exists(directory):
		os.makedirs(directory)
	return path

html = urlopen('http://www.pythonscraping.com')
bsObj = BeautifulSoup(html, 'html5lib')
downloadList = bsObj.findAll(src = True)
for download in downloadList:
	fileUrl = getAbosulateUrl(baseUrl, download['src'])
	if fileUrl is not None:
		print(fileUrl)
		




