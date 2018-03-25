from selenium import webdriver
import time


class NJUSETool:
    def __init__(self, user, password):
        self.user = user
        self.password = password

    def login(self):
        driver = webdriver.Chrome()
        driver.get('http://218.94.159.99/login/index.php')
        time.sleep(3)
        driver.find_element_by_id('username').clear()
        driver.find_element_by_id('username').send_keys(self.user)
        driver.find_element_by_id('password').clear()
        driver.find_element_by_id('password').send_keys(self.password)
        driver.find_element_by_id('loginbtn').click()


tool = NJUSETool('username', 'password')
tool.login()

