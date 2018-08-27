from selenium import webdriver
import time
from PIL import Image, ImageEnhance
import pytesseract as pyt


# 进入南京大学教务处看成绩...近几天有个烦人的核查信息，注意点击确认后才可进一步核查（5s内完成否则抱异常），顺利自动跳转成绩页面
picture_path = 'pictures/code_picture.png'
code_path = 'pictures/code.png'


class NJUTool:
    def __init__(self, user='', password=''):
        url = 'http://elite.nju.edu.cn/jiaowu/'
        driver = webdriver.Chrome()
        driver.get(url)
        self.driver = driver
        time.sleep(3)
        self.user = user
        self.password = password
        print('Enter the sec_code')
        self.val_code = input()

    def login(self):
        driver = self.driver
        driver.find_element_by_id('userName').clear()
        driver.find_element_by_id('userName').send_keys(self.user)
        driver.find_element_by_id('password').clear()
        driver.find_element_by_id('password').send_keys(self.password)
        driver.find_element_by_id('ValidateCode').clear()

        driver.find_element_by_id('ValidateCode').send_keys(self.val_code)
        driver.find_element_by_css_selector('.Btn').click()
        time.sleep(5)

    def check_grade(self):
        url = 'http://elite.nju.edu.cn/jiaowu/student/studentinfo/achievementinfo.do?method=searchTermList'
        self.driver.get(url)

    def recognize_val_code(self):
        driver = self.driver
        driver.get_screenshot_as_file(picture_path)  # 比较好理解
        im = Image.open(picture_path)
        box = (561, 699, 717, 729)  # 设置要裁剪的区域
        region = im.crop(box)
        region.save(code_path)
        im = Image.open(code_path)
        imgry = im.convert('L')  # 图像加强，二值化
        sharpness = ImageEnhance.Contrast(imgry)  # 对比度增强
        sharp_img = sharpness.enhance(2.0)
        sharp_img.save(code_path)

        code = pyt.image_to_string(im)
        return code


tool = NJUTool('1612500xx', 'xxxxxx')
tool.login()
tool.check_grade()
