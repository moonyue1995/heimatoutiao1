# -*- coding: utf-8 -*-
"""
@Time ： 2021-10-20 10:24
@Auth ： 一条咸鱼
@File ：main_page.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
统一资源入口类
"""
from page.page_address import PageAddress
from page.page_content import PageContent
from page.page_login import PageLogin

from tools import get_log

log = get_log.GetLog.get_logger()


class MainPage:

    def __init__(self, driver):
        self.driver = driver

    # 定义登陆入口方法
    def main_login(self):
        log.info("正在对初始化统一入口类")
        return PageLogin(self.driver)

    # 定义发布文章入口方法
    def main_content(self):
        return PageContent(self.driver)

    # 定义跳转git页面方法
    def main_git(self):
        return PageAddress(self.driver)
