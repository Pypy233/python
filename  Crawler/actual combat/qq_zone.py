# qq空间的信息, 使用Chrome，Safari不能找到输入密码的框emmmm...

from selenium import webdriver
from bs4 import BeautifulSoup
import time


class QQZoneTool():
    def __init__(self, user, password):
        self.user = user
        self.password = password

    # 头像登录或者用户名密码登录
    def login(self):
        driver = webdriver.Chrome()
        driver.get('http://user.qzone.qq.com/' + self.user + '/311')
        time.sleep(5)
        driver.switch_to.frame('login_frame')
        try:
            driver.find_element_by_css_selector('#img_out_' + self.user).click()
            print('Image login...')
        except:
            print('Fail to login by image...')

        try:
            driver.find_element_by_id('login_div')
            find_login = True
        except:
            find_login = False
        if find_login:
            driver.find_element_by_id('switcher_plogin').click()
            driver.find_element_by_id('u').clear()  # 选择用户名框
            driver.find_element_by_id('u').send_keys(self.user)
            driver.find_element_by_id('p').clear()
            driver.find_element_by_id('p').send_keys(self.password)
            driver.find_element_by_id('login_button').click()
            time.sleep(3)

        return driver

    def access_friend_zone(self, friend_qq):
        driver = self.login()
        try:
            accept = driver.get('http://user.qzone.qq.com/' + friend_qq + '/311'.format(friend_qq))
            accept = True
        except:
            accept = False
            print('Fail to accept access to qq zone...')
        driver.switch_to.frame('app_canvas_frame')
        time.sleep(3)  # 必要的等待
        return driver

    # 参考洲神的代码，emmm没有考虑翻页，过几天完善
    def get_friend_shuoshuo(self, friend_qq):
        driver = self.access_friend_zone(friend_qq)
        text_content = driver.find_elements_by_css_selector('.content')
        shuoshuo_time = driver.find_elements_by_css_selector('.c_tx.c_tx3.goDetail')
        for con, sti in zip(text_content, shuoshuo_time):
            data = {
                'time': sti.text,
                'content': con.text
            }
            print(data)

        driver.close()
        driver.quit()

    # 点赞狂魔，emmm可能会被打
    def like_friend(self, friend_qq):
        driver = self.access_friend_zone(friend_qq)
        time.sleep(2)
        driver.find_elements_by_xpath('./div[3]/div[1]/p/a[3]')

        driver.close()
        driver.quit()


