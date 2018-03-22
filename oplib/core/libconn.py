# -*- coding: utf-8 -*-
# author:xiaoming
from libcloud.compute.providers import get_driver
from libcloud.compute.types import Provider
from core.tools import file_read,error_info
import os
# PATH=os.path.dirname(os.path.dirname(__file__))
# import sys
# sys.path.insert(0,PATH)

def op_lib_conn():
    PATH = os.path.dirname(os.path.dirname(__file__))
    filename='%s/db/%s'%(PATH,'op_connect.json')
    print(filename)
    data=file_read(filename)
    print(data)
    if not data=='':
        auth_username = data.get('auth_username')
        auth_password = data.get('auth_password')
        auth_url = data.get('auth_url')
        project_name = data.get('project_name')
        domain_name= data.get('domain_name')
        region_name = data.get('region_name')
        provider = get_driver(Provider.OPENSTACK)
        return provider(auth_username,
                        auth_password,
                        ex_force_auth_url=auth_url,
                        ex_force_auth_version='3.x_password',
                        ex_tenant_name=project_name,
                        ex_domain_name=domain_name,
                        ex_force_service_region=region_name)
    else:
        error_info('文件不存在')
        return 0
# conn=op_lib_conn()
# print(conn)
# images = conn.list_images()
# print(images)

# auth_username = 'admin'
# auth_password = '000000'
# auth_url = 'http://%s:5000'%'controller'
# project_name = 'admin'
# domain_name='domain'
# region_name = 'RegionOne'

