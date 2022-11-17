#!usr/bin/python
# -*- coding: utf-8 -*-
# 导入模块
import xlrd

# 打开文件方式1：
work_book = xlrd.open_workbook('/home/li/error.xlsx')
print(work_book)
sheet_1 = work_book.sheet_by_index(0)
print(sheet_1)

# 获取sheet表单元格对象，单元格数据类型：单元格值
cell_0 = sheet_1.cell(0,0)
print(cell_0)
# ------运行结果------
# text:'日期'
# ------运行结果------

# 获取sheet表单元格值
cell_0_value = sheet_1.cell_value(0,0)
print(cell_0_value)
# ------运行结果------
# 日期
# ------运行结果------

# 获取单元格类型
cell_0_type = sheet_1.cell_type(0,0)
print(cell_0_type)
# ------运行结果------
# 1
# ------运行结果------

colums = 2
rows = 456

errorArray = []

for i in range(rows):
    ce_value = sheet_1.cell_value(i,0)
    ice_value = sheet_1.cell_value(i,1)
    print(i,ce_value,ice_value)
    errorDict = {}
    errorDict['ec'] = ce_value
    errorDict['iec'] = ice_value
    errorArray.append(errorDict)


# write into yaml
