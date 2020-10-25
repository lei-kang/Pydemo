# -*- coding: utf-8 -*-
# @Time : 2020/10/25 19:40
# @Author : kang
# @File : add_menber_page.py
# @Software: PyCharm
from selenium.webdriver.common.by import By

from web.podemo.page.base_page import BasePage


class AddMenberPage(BasePage):

    def add_menber(self,username,acctid,phone):
        self.find(By.CSS_SELECTOR, "#username").send_keys(username)
        self.find(By.CSS_SELECTOR, "#memberAdd_acctid").send_keys(acctid)
        self.find(By.CSS_SELECTOR,"#memberAdd_phone").send_keys(phone)
        self.find(By.CSS_SELECTOR,".js_btn_save").click()
        return True

    def get_menber(self):
        pass