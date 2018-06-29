# -*- coding: utf-8 -*-
# author:xiaoming
# import os
# PATH=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(PATH)
# import sys
# sys.path.insert(0,PATH)
from core.tools import file_read, error_info
def auth_dict():
    '''获取认证数据'''
    import os
    PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    filename='%s/db/%s'%(PATH,'op_connect.json')
    data=file_read(filename)
    return data
def lib_conn(obj_type='compute'):
    data=auth_dict()
    if not data=='':
        if obj_type == 'compute':
            '''apache lib openstack_api connect'''
            from libcloud.compute.providers import get_driver
            from libcloud.compute.types import Provider
            provider = get_driver(Provider.OPENSTACK)
        elif obj_type == 'swift':
            '''apache lib swift connect'''
            from libcloud.storage.types import Provider
            from libcloud.storage.providers import get_driver
            provider = get_driver(Provider.OPENSTACK_SWIFT)
        else:
            return 0
        return provider(data.get('auth_username'),
                        data.get('auth_password'),
                        ex_force_auth_url=data.get('auth_url'),
                        ex_force_auth_version='3.x_password',
                        ex_tenant_name=data.get('project_name'),
                        ex_domain_name=data.get('domain_name'),
                        ex_force_service_region=data.get('region_name'))
    else:
        error_info('文件不存在')
        return 0
# print(conn)
# conn=op_lib_conn()
# for i in dir(conn):
#     print(i)
# images = conn.list_images()
# networks=conn.ex_list_networks()
# print(networks)



# auth_username = 'admin'
# auth_password = '000000'
# auth_url = 'http://%s:5000'%'controller'
# project_name = 'admin'
# domain_name='domain'
# region_name = 'RegionOne'

