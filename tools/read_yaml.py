# -*- coding: utf-8 -*-
"""
@Time ： 2021-10-21 14:13
@Auth ： 一条咸鱼
@File ：read_yaml.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)

"""
import yaml

from config import BASE_PATH
import os


def read_yaml(filename, key):
    filepath = BASE_PATH + os.sep + "data" + os.sep + filename
    with open(filepath, "r", encoding="utf-8") as f:
        list = []
        data = yaml.load(f)[key]
        for i in data.values():
            list.append(i)

    return list


if __name__ == '__main__':
    print(read_yaml("login_data.yaml", "test01_login"))

