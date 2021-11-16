# -*- coding: utf-8 -*-
"""
@Time ： 2021-10-22 14:58
@Auth ： 一条咸鱼
@File ：page_content.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
发布文章 page 页
"""
from time import sleep

import page
from base.base import Base
from base.web_base import WebBase


class PageContent(WebBase):

    def __init__(self, driver):
        self.driver = driver

    # 点击 内容管理按钮
    def page_content_management(self):
        self.base_click(page.content_management)

    # 点击发表文章按钮
    def page_content_article(self):
        sleep(1)
        self.base_click(page.content_article)

    # 点击标题，并输入
    def page_content_title(self, values):
        self.base_input(page.content_title, values)

    # 先切换到frame，输入内容，返回到主frame
    def page_content_text(self, value):
        # 切换到 frame
        self.base_switch_frame(page.content_frame)
        # 点击输入框按钮并输入
        self.base_input(page.content_text, value)
        # 返回到默认frame
        self.base_switch_default_frame()

    # 点击选择图片按钮
    def page_content_select_img(self):
        self.base_click(page.content_img)

    # 本地上传

    def page_select_img(self):
        self.base_click(page.content_select_img)
        target = self.base_find_element(page.content_OK_btu)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)
        self.base_click(page.content_OK_btu)

    # 选择频道

    def page_content_channel(self):
        target = self.base_find_element(page.choose)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)  # 拖动到可见的元素去
        # 这个方法可以将滚动条拖动到需要显示的元素位置，此方法用途比较广，可以使用
        self.web_base_click("请选择", "软件测试")

    def page_content_all(self, values, value):
        self.page_content_management()
        sleep(3)
        self.page_content_article()
        sleep(3)
        self.page_content_title(values)
        sleep(3)
        self.page_content_text(value)
        sleep(3)
        self.page_content_select_img()
        sleep(3)
        self.page_select_img()
        sleep(3)
        # self.page_content_channel()
        sleep(3)
