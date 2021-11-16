# -*- coding: utf-8 -*-
"""
@Time ： 2021-10-20 09:35
@Auth ： 一条咸鱼
@File ：test01_login.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
脚本层：
"""

import pytest

import page
from page.main_page import MainPage

from tools.getdriver import GerDriver
from tools.read_excel import read_excel
from tools.read_yaml import read_yaml


class TestLogin:
    @classmethod
    def setup_class(cls):
        cls.driver = GerDriver.get_driver(page.url)
        cls.login = MainPage(cls.driver).main_login()

    @classmethod
    def teardown_class(cls):
        GerDriver.quit_driver()

    # @pytest.mark.parametrize("args", read_yaml("login_data.yaml", "test01_login"))
    @pytest.mark.parametrize("args", read_excel())
    def test01_login_all(self, args):
        username = args["username"]
        code = args["code"]
        expect = args["expect"]
        state = args["state"]

        print("打印一下状态信息：", state)

        if state == "true":
            self.login.page_login_all(username, code)
            try:
                assert expect == self.login.base_get_text(page.login_success)

            except Exception as e:

                self.login.base_get_img()
                raise

            self.login.page_logout()

        else:
            print("-----------走到这了----------",self.login.base_get_text(page.login_click))
            try:
                self.login.page_login_all(username, code)
                assert expect == self.login.base_get_text(page.login_click)
            except Exception as e:

                self.login.base_get_img()