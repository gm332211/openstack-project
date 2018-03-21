# -*- coding: utf-8 -*-
# author:xiaoming
def help_list(data=None):
    '''帮助 :已完成'''
    from conf.setting import help_dic
    if data:
        help_dic.get(data)
        for key in help_dic[data]:
            str_data='%s %s'%(data,key)
            print_version(str_data)
    else:
        for key in help_dic:
            for i in help_dic[key]:
                # print(key,i,help_dic[key][i])
                str_data = '%s %s %s' % (key,i,help_dic[key][i])
                print_version(str_data)
    exit()
def out_beautiful(data):
    print('----%s----' % (data))
def print_version(data):
    import sys
    py_version = sys.version_info.major
    if py_version=='2':
        pass
    print(data)