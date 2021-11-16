# -*- coding: utf-8 -*-
"""
@Time ： 2021-10-24 10:28
@Auth ： 一条咸鱼
@File ：updown_img.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
from time import sleep

import pyperclip
from pykeyboard import PyKeyboard
from pymouse import PyMouse

from tools.get_log import GetLog
Log = GetLog.get_logger()

class UpdownImg:
    def send_pictures(self, loc, img_name, file):
        """
        上传图片
        :param loc: 元素
        :param img_name: 图片名称
        :param file: 图片路径
        :return:
        """

        def _is_China(file):

            # 判断文件名称中是否包含中文，官方库要求必须文件路径为英文，否则会抛异常，所以单独加了一层判断
            for ch in file:
                if u'\u4e00' <= ch <= u'\u9fff':
                    return True

            return False

        try:
            if _is_China(file) is True:
                # 这个是我自己单独封装的Log日志打印，如果没有封装，可以直接用print代替
                Log.logger.error("文件路径中不允许包含中文字符！请修改文件命名。文件路径:{0}".format(file))

            if _is_China(file) is False:
                Log.logger.info("开始上传图片, 图片路径:{0}".format(file))

                self.click_element(loc, img_name)
                k = PyKeyboard()

                m = PyMouse()
                filepath = '/'
                # 模拟键盘点击 Command + Shift + G
                k.press_keys(['Command', 'Shift', 'G'])

                # 获取当前屏幕尺寸
                x_dim, y_dim = m.screen_size()
                m.click(x_dim // 2, y_dim // 2, 1)

                # 复制文件路径开头的斜杠/，如果不加斜杠的话，脚本会缺少头部的斜杠
                pyperclip.copy(filepath)

                # 粘贴斜杠/
                k.press_keys(['Command', 'V'])
                # 输入文件全路径进去
                k.type_string(file)
                sleep(2)
                k.press_key('Return')
                sleep(2)
                k.press_key('Return')
                sleep(2)

        except:
            # 单独封装了一个selenium 失败截图的功能
            self.save_page_shots(img_name)
            Log.logger.error("上传图片失败!图片路径{0}".format(file))
            raise