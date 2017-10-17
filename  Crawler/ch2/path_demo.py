from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
html = urlopen("http://qinggongxiao.nju.edu.cn/cys/index.html")
bsObj = BeautifulSoup(html, 'html5lib')
images = bsObj.findAll('img', {'src': re.compile("\.\./img/gifts/img.*\.jpg")})
for i in images:
	print(i['src'])

