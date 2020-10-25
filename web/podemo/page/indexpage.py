# -*- coding: utf-8 -*-
# @Time : 2020/10/25 19:38
# @Author : kang
# @File : indexpage.py
# @Software: PyCharm
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement

from web.podemo.page.add_menber_page import AddMenberPage
from web.podemo.page.base_page import BasePage
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class IndexPage(BasePage):
    base_url = "https://work.weixin.qq.com/wework_admin/frame#index"
    def goto_menber(self):
        self.find(By.CSS_SELECTOR,"#menu_contacts").click()
        locator = (By.CSS_SELECTOR, ".js_has_member>div:nth-child(1)>a:nth-child(2)")
        # element:WebElement = WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(locator))
        # self.find(By.CSS_SELECTOR, ".js_has_member>div:nth-child(1)>a:nth-child(2)").click()
        self.wait(locator).click()
        # 借助WebDriverWait 显示等待判断跳转按钮是否可以点击，同时判断是否跳转成功即茶轴跳转后的一个元素
        # def wait_for_next(x: WebDriver):
        #     try:
        #         x.find_element(*locator).click()
        #         return x.find_element(By.ID, "username")
        #     except:
        #         return False
        #
        # WebDriverWait(self.driver, 10).until(wait_for_next)
        return AddMenberPage(self.driver)
