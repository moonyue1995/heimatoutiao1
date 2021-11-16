# -*- coding: utf-8 -*-
"""
@Time ： 2021-10-20 09:32
@Auth ： 一条咸鱼
@File ：base.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
操作层：存放对元素的操作，定义方法
"""
import time

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from tools import get_log

log = get_log.GetLog.get_logger()


class Base:

    # 初始化 driver ，后期谁去调用，谁去传递参数

    def __init__(self, driver):
        log.info("正在初始化driver {}".format(driver))
        self.driver = driver

    # 定义 查找元素方法
    # 通过显示等待的方法，进行查找 ,*ele 对 元组的一个解析
    def base_find_element(self, ele, timeout=30, poll=0.5):
        log.info("查找元素的方法{}".format(ele))
        element = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(lambda x: x.find_element(*ele))
        # element = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(EC.presence_of_element_located(ele))
        if element:
            return element
        else:
            print("没有该元素")

    # 定义输入方法
    def base_input(self, ele, values):
        e = self.base_find_element(ele)
        # 输入框清除 的三种方法
        #     1. clear（） 方法
        #     2。keys 通过 全选，在删除
        #     3。通过 actionChains 方法 双击
        # e.send_keys(Keys.CONTROL + 'a')  # 全选
        # #
        # e.send_keys(Keys.DELETE)  # 删除

        # 清除输入框
        log.info("正在对元素进行清空操作：")
        e.clear()
        # 输入内容
        # js = 'document.querySelector("{}").value=""'.format(page.login_username_01)
        # self.driver.execute_script(js)
        # ActionChains(self.driver).double_click(e).perform()

        # js = 'document.querySelector({e}).value="";'.format(e=e)
        # self.driver.execute_script(js)
        log.info("正在对元素进行输入操作".format(values))
        e.send_keys(values)

    # 定义点击方法
    def base_click(self, ele):
        log.info("正在对元素进行点击操作".format(ele))
        self.base_find_element(ele).click()

    # 获取界面元素文字方法
    def base_get_text(self, ele):
        log.info("正在获取元素信息".format(ele))
        return self.base_find_element(ele).text

    # 获取错误截图的方法
    def base_get_img(self):

        self.driver.get_screenshot_as_file("./img/img{}.png".format(time.strftime("%Y%m%d-%H%M%S")))
        # self.__base_write_img()

    # def __base_write_img(self):
    #     with open("./img/img.png", "rb") as f:
    #         allure.attach("错误原因", f.read(), allure.attachment_type.PNG)

    # 创建切换 iframe 的方法
    def base_switch_frame(self, ele):
        ele1 = self.base_find_element(ele)
        self.driver.switch_to.frame(ele1)

    # 回到默认frame 方法
    def base_switch_default_frame(self):
        self.driver.switch_to.default_content()

    # 跳转到新的标签页

    def base_switch_to_windows(self, title):

        handle = self.base_get_title_handle(title)

        self.driver.switch_to.window(handle)

    # 使用句柄的方法

    def base_get_title_handle(self, title):

        for handles in self.driver.window_handles:

            self.driver.switch_to.window(handles)

            if self.driver.title == title:
                return handles
