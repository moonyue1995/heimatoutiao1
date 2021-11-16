# -*- coding: utf-8 -*-
"""
@Time ： 2021-11-12 13:56
@Auth ： 一条咸鱼
@File ：read_excel.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
读取 Excel 数据文件
"""

import xlrd


class Read_excel():

    def read_excel(self):
        book = xlrd.open_workbook("/Users/bunsuketake/Desktop/台账.xls")

        sel = book.sheet_by_name("Sheet2")
        rows = sel.nrows
        dict_list = []

        for i in range(1, rows):
            dict_list.append(sel.row_values(i))

        return dict_list


if __name__ == '__main__':
    print(Read_excel().read_excel())
