# -*- coding: utf-8 -*-
"""
@Time ： 2021-10-20 09:34
@Auth ： 一条咸鱼
@File ：page_login.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
业务层：实现具体的业务逻辑
"""
from time import sleep

from selenium.webdriver.common.by import By

import page
from base.base import Base
from tools import get_log

log = get_log.GetLog.get_logger()


class PageLogin(Base):

    # 定义输入用户名方法
    def page_input_username(self, username):
        log.info("输入用户名".format(username))
        self.base_input(page.login_username, username)

    # 定义输入验证码方法
    def page_input_verify_code(self, code):
        log.info("输入验证码".format(code))
        self.base_input(page.login_code, code)

    # 定义点击方法定义点击方法
    def page_login_click(self):
        log.info("点击登陆按钮")
        self.base_click(page.login_click)

    # 退出登陆方法
    def page_logout(self):
        self.base_click(page.login_X)
        self.base_click(page.login_success_username)
        sleep(5)
        self.base_click(page.login_quit)

    def page_X(self):
        self.base_click(page.login_X)
        self.base_click(page.login_success_username)
        sleep(5)

    # 业务整合

    def page_login_all(self, username, code):
        self.page_input_username(username)
        sleep(3)
        self.page_input_verify_code(code)
        sleep(3)
        self.page_login_click()
        sleep(3)
