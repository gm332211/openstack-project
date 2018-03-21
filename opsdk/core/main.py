# -*- coding: utf-8 -*-
# author:xiaoming
from core import views
from core.tools import help_list
import sys
def run():
    #检测对象是否存在,检查是否有参数
    handle=views.handle
    argv=sys.argv[1:]
    argv_list=[]
    argv_len=len(argv)
    if argv_len < 1:
        print('请输入命令')
        help_list()
    if argv[0] not in handle:
        print('没有这个命令')
        help_list()
    if argv_len < 2:
        print('命令不完整')
        help_list()
    sub_handle=handle.get(argv[0])
    if argv[1] not in sub_handle:
        help_list(argv[0])
    if argv_len > 2:
        argv_list=argv[2:]
    # try:
    handle[argv[0]][argv[1]](argv_list)
    # except Exception as e:
    #     print(e)
    #     views.help_list()