# -*- coding: utf-8 -*-
"""
@Time ： 2021-11-13 15:03
@Auth ： 一条咸鱼
@File ：testDemo.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""

import unittest

import page
from page.main_page import MainPage
from tools.getdriver import GerDriver
from ddt import ddt, unpack, data

from tools.read_excel import Read_excel


class TestLogin(unittest.TestCase):

    def setUp(self):
        self.driver = GerDriver().get_driver(page.url)

        self.login = MainPage(self.driver).main_login()
        print("吨年gina",Read_excel().read_excel())

    def tearDown(self):
        GerDriver.quit_driver()

    @data(Read_excel().read_excel())
    @unpack
    def test01_login(self, data):
        username, code, expect, state = data
        print("===========", username)
        print("===========", code)
        print("===========", expect)
        if state == "true":
            self.login.page_login_all(username, code)
            try:
                assert expect == self.login.base_get_text(page.login_success)

            except Exception as e:

                self.login.base_get_img()
                raise

            self.login.page_logout()

        else:
            print("-----------走到这了----------", self.login.base_get_text(page.login_click))
            try:
                self.login.page_login_all(username, code)
                assert expect == self.login.base_get_text(page.login_click)
            except Exception as e:

                self.login.base_get_img()
