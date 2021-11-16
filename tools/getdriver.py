# -*- coding: utf-8 -*-
"""
@Time ： 2021-10-20 10:02
@Auth ： 一条咸鱼
@File ：getdriver.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""

from selenium import webdriver


class GerDriver:
    driver = None

    @classmethod
    def get_driver(cls, url):
        if cls.driver is None:
            cls.driver = webdriver.Chrome()
            cls.driver.maximize_window()
            cls.driver.get(url)
        return cls.driver

    @classmethod
    def quit_driver(cls):
        if cls.driver:
            cls.driver.quit()
            cls.driver = None
