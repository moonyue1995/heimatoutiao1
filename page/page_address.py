# -*- coding: utf-8 -*-
"""
@Time ： 2021-10-28 15:08
@Auth ： 一条咸鱼
@File ：page_address.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
页面层
"""
import page
from base.web_base import WebBase


class PageAddress(WebBase):

    # 点击 git地址方法
    def git_git_address(self):
        self.base_click(page.git_Git)

    def git_get_text(self):
        self.base_switch_to_windows(page.git_Git_title)

        return self.base_get_text(page.git_new_code)
