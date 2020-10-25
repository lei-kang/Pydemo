# -*- coding: utf-8 -*-
# @Time : 2020/10/25 19:30
# @Author : kang
# @File : base_page.py
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage():
    base_url = ""
    def __init__(self,driver:WebDriver=None):
        if driver == None:
            options = Options()
            options.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=options)
            self.driver.implicitly_wait(5)
            # self.driver = webdriver.Chrome()
        else:
            self.driver = driver

        if self.base_url != "":
            self.driver.get(self.base_url)

    def find(self,by,local):
        return self.driver.find_element(by,local)

    def finds(self,by,local):
        return self.driver.find_elements(by,local)