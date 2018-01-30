# 爬取豆瓣的一些电影信息
from urllib import request
import ssl
from bs4 import BeautifulSoup as bs
import re

ssl._create_default_https_context = ssl._create_unverified_context
resp = request.urlopen('https://movie.douban.com/nowplaying/hangzhou/')
html_data = resp.read().decode('utf-8')
# print(html_data)
soup = bs(html_data, 'html.parser')
now_playing_movie = soup.find_all('div', id='nowplaying')
# print(now_playing_movie)
# print(len(now_playing_movie))
now_playing_movie_list = now_playing_movie[0].find_all('li', class_='list-item')
# print(now_playing_movie_list)
now_playing_list = []
for item in now_playing_movie_list:
    now_playing_dict = {'id': item['data-subject']}
    for tag_img_item in item.find_all('img'):
        now_playing_dict['name'] = tag_img_item['alt']
        now_playing_list.append(now_playing_dict)

print(now_playing_list)

requrl = 'https://movie.douban.com/subject/' + \
         now_playing_list[0]['id'] + '/comments' +'?' +'start=0' + '&limit=20'
resp = request.urlopen(requrl)
html_data = resp.read().decode('utf-8')
soup = bs(html_data, 'html.parser')
common_div_list = soup.find_all('div', class_='comment')

each_comment_item = []
for item in common_div_list:
    if item.find_all('p')[0] is not None:
        each_comment_item.append(item.find_all('p')[0].string)

print(each_comment_item)

comments = ''
for i in range(len(each_comment_item)):
    comments += str(each_comment_item[i]).strip()

print(comments)

# 删去标点
pattern = re.compile(r'[\u4e00-\u9fa5]+')
data = re.findall(pattern, comments)
clear_comments = ''.join(data)
print(clear_comments)