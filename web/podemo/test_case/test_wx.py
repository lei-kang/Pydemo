# -*- coding: utf-8 -*-
# @Time : 2020/10/25 19:54
# @Author : kang
# @File : test_wx.py
# @Software: PyCharm
from time import sleep

import pytest

from web.podemo.page.indexpage import IndexPage


class TestWx():

    def setup(self):
        self.index = IndexPage()


    # 测试添加练习人
    # @pytest.mark.parametrize("username,acctid,phone",[["测试","123","123"]])
    def test_wx_add(self):
        username = "测是"
        acctid = "123"
        phone ="123"
        add = self.index.goto_menber()
        assert add.add_menber(username,acctid,phone)