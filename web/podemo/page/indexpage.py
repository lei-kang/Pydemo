# -*- coding: utf-8 -*-
# @Time : 2020/10/25 19:38
# @Author : kang
# @File : indexpage.py
# @Software: PyCharm
from selenium.webdriver.common.by import By

from web.podemo.page.add_menber_page import AddMenberPage
from web.podemo.page.base_page import BasePage


class IndexPage(BasePage):

    def goto_menber(self):
        self.find(By.CSS_SELECTOR,"#menu_contacts").click()
        self.find(By.CSS_SELECTOR, ".qui_btn ww_btn js_add_member").click()
        return AddMenberPage(self.driver)
