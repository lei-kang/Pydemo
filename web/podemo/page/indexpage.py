# -*- coding: utf-8 -*-
# @Time : 2020/10/25 19:38
# @Author : kang
# @File : indexpage.py
# @Software: PyCharm
from time import sleep

from selenium.webdriver.common.by import By

from web.podemo.page.add_menber_page import AddMenberPage
from web.podemo.page.base_page import BasePage


class IndexPage(BasePage):
    base_url = "https://work.weixin.qq.com/wework_admin/frame#index"
    def goto_menber(self):
        self.find(By.CSS_SELECTOR,"#menu_contacts").click()
        sleep(2)
        self.find(By.CSS_SELECTOR, ".js_has_member>div:nth-child(1)>a:nth-child(2)").click()
        return AddMenberPage(self.driver)
