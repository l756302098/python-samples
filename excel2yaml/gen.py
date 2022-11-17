#!usr/bin/python
# -*- coding: utf-8 -*-
# 导入模块
import yaml
import xlrd

work_book = xlrd.open_workbook('/home/li/error.xlsx')
print(work_book)
sheet_1 = work_book.sheet_by_index(0)
print(sheet_1)

colums = 2
rows = 456

errorArray = []

for i in range(rows):
    ice_value = str(sheet_1.cell_value(i,0))
    ce_value = '0x' + str(sheet_1.cell_value(i,1))
    print(i,ce_value,ice_value)
    if ice_value == '0.0' or ice_value == '0':
        ice_value = '0x00'
    else:
        ice_value = '0x' + ice_value
    #print(i,ce_value,ice_value)
    errorDict = {}
    errorDict['ec'] = ce_value
    errorDict['iec'] = ice_value
    errorArray.append(errorDict)

data={'maps':errorArray}

with open('/home/li/error.yaml', 'w') as file:
    yaml.dump(data, file)

# print(open('/home/li/error.yaml').read())