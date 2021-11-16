# -*- coding: utf-8 -*-
"""
@Time ： 2021-10-22 15:04
@Auth ： 一条咸鱼
@File ：test02_content.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
import page
from page.main_page import MainPage
from tools.getdriver import GerDriver


class TestContent():

    @classmethod
    def setup_class(cls):
        cls.driver = GerDriver.get_driver(page.url)

        cls.content = MainPage(cls.driver).main_content()

        MainPage(cls.driver).main_login().page_login_all("", "")

    @classmethod
    def teardown_class(cls):
        GerDriver.quit_driver()

    def test_content(self):
        self.content.page_content_all(values="这是个小米呀", value="这还是个小米呀")
