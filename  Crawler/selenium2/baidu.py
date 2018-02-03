from selenium import webdriver
import time


class BaiduTool:
    def __init__(self, url = 'http://baidu.com'):
        driver = webdriver.Chrome()
        driver.get(url)
        self.driver = driver
        time.sleep(3)

    def search(self, search_content):
        driver = self.driver
        driver.find_element_by_id('kw').clear()
        driver.find_element_by_id('kw').send_keys(search_content)
        driver.find_element_by_id('su').click()


tool = BaiduTool()
tool.search('人')