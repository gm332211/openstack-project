# -*- coding: utf-8 -*-
# author:xiaoming
import json,os
def file_write(filename,data):
    '''json写入'''
    print(filename)
    f=open(filename,'w')
    json.dump(data,f)
    f.close()
def file_read(filename):
    '''json读取'''
    data=''
    if os.path.isfile(filename):
        f = open(filename, 'r')
        data = json.load(f)
        f.close()
    return data
def error_info(data):
    '''报错反馈'''
    print(data)