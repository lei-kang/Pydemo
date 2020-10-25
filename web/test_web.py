# -*- coding = utf-8 -*-
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains, TouchActions
from selenium.webdriver.common.by import By
import pytest


class TestTouchAction():

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(3)
    def teardown(self):
        self.driver.quit()

    def test_case_scroll(self):
        self.driver.get("https://www.baidu.com")
        self.driver.execute_script('')
        sleep(5)
