# qq空间的信息, 使用Chrome，Safari不能找到输入密码的框emmmm...

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


class QQZoneTool():
    def __init__(self, user, password):
        driver = webdriver.Chrome()
        driver.get('http://user.qzone.qq.com/' + user + '/311'.format())
        time.sleep(5)
        try:
            driver.find_element_by_id('login_div')
            find_login = True
        except:
             find_login = False
        if find_login:
            driver.switch_to.frame('login_frame')
            driver.find_element_by_id('switcher_plogin').click()
            driver.find_element_by_id('u').clear()  # 选择用户名框
            driver.find_element_by_id('u').send_keys(user)
            driver.find_element_by_id('p').clear()
            driver.find_element_by_id('p').send_keys(password)
            driver.find_element_by_id('login_button').click()
            time.sleep(3)
        driver.implicitly_wait(3)


