# -*- coding: utf-8 -*-
"""
@Time ： 2021-10-28 15:43
@Auth ： 一条咸鱼
@File ：test03_git.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
import page
from page.main_page import MainPage
from tools.getdriver import GerDriver


class TestGit():
    @classmethod
    def setup_class(cls):
        cls.driver = GerDriver().get_driver(page.url)
        cls.git = MainPage(cls.driver).main_git()
        MainPage(cls.driver).main_login().page_login_all("", "")

        cls.login = MainPage(cls.driver).main_login()

    @classmethod
    def teardown_class(cls):
        GerDriver().quit_driver()

    def test_git(self):
        self.login.page_X()
        self.git.git_git_address()
        print("==============",self.git.git_get_text())
        assert "code" == self.git.git_get_text()
