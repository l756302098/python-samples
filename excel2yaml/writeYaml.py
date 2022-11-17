#!usr/bin/python
# -*- coding: utf-8 -*-
# 导入模块
import yaml

errorArray = []
dict1 = {}
dict1['ec'] = 1
dict1['iec'] = 1
errorArray.append(dict1)
dict2 = {}
dict2['ec'] = 2
dict2['iec'] = 2
errorArray.append(dict2)

data={'maps':errorArray}

with open('/home/li/error.yaml', 'w') as file:
    yaml.dump(data, file)

print(open('/home/li/error.yaml').read())
