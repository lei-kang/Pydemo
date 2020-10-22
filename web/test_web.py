# -*- coding = utf-8 -*-
import time

from selenium import webdriver
from selenium.webdriver import ActionChains, TouchActions
from selenium.webdriver.common.by import By
import pytest





class TestTouchAction():

    def setup(self):
        # self.options = webdriver.ChromeOptions()
        # self.options.binary_location = r'C:\Users\Administrator\AppData\Local\Google\Chrome\Application\chrome.exe'
        opt = webdriver.ChromeOptions()
        opt.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(chrome_options=opt)
        self.driver.maximize_window()  ## 浏览器最大化
        self.driver.implicitly_wait(5)  ## 隐式等待

    def teardown(self):
        self.driver.quit()

    def test_case_scroll(self):
        self.driver.get("https://www.baidu.com")
        edit = self.driver.find_element(By.XPATH,'//*[@id="kw"]')
        action = TouchActions(self.driver)
        action.tap(edit)
        edit.send_keys("selenium测试")
        time.sleep(5)
        # element_click = self.driver.find_element(By.XPATH, '//*[@id="su"]')
        # action.tap(element_click)
        # time.sleep(5)
        action.perform()
        # action.scroll_from_element(element_click,0,1000).perform()