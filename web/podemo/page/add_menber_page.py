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

    def get_member(self, value):
        # 验证联系人添加成功
        total_list = []
        while True:
            contactlist = self.finds(By.CSS_SELECTOR, '.member_colRight_memberTable_td:nth-child(2)')
            titlelist = [element.get_attribute("title") for element in contactlist]
            print(titlelist)
            if value in titlelist:
                return True
            total_list = total_list + titlelist

            result: str = self.find(By.CSS_SELECTOR, ".ww_pageNav_info_text").text
            num, total = result.split('/', 1)

            if int(num) == int(total):
                return False
            else:
                self.find(By.CSS_SELECTOR, ".ww_commonImg_PageNavArrowRightNormal").click()

        return total_list