# -*- coding: utf-8 -*-
"""
@Time ： 2021-10-25 10:54
@Auth ： 一条咸鱼
@File ：web_base.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
from selenium.webdriver.common.by import By

from base.base import Base


class WebBase(Base):

    # web 的 私有方法
    def web_base_click(self, choose, click_text):
        ele = By.XPATH, "//input[@placeholder='{}']".format(choose)
        self.base_click(ele)

        # 3. 点击包含显示文本的元素
        loc = By.XPATH, "//*[text()='{}']".format(click_text)
        self.base_click(loc)
