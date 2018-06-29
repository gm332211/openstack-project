# -*- coding: utf-8 -*-
# author:xiaoming
'''openstack_api 连接文件'''
from core.connect_set import show_openstack_connection_now
def op_connectionv2(data):
    '''python2 openstack_sdk连接'''
    from openstack import connection
    region = data['region']
    auth_url = data['auth_url']
    username = data['username']
    password = data['password']
    tenant_name = data['tenant_name']
    domain_name = data['domain_name']
    return connection.Connection(
        region_name=region,
        auth=dict(
            auth_url=auth_url,
            username=username,
            password=password,
            project_name=tenant_name,
            project_domain_name=domain_name,
            user_domain_name=domain_name),
        compute_api_version='2',
        identity_api_version='3',
        identity_interface='internal')
def op_connectionv3(data):
    '''python3 openstack_sdk连接 :已完成'''
    from openstack import profile
    from openstack import connection
    region = data['region']
    auth_url = data['auth_url']
    username = data['username']
    password = data['password']
    tenant_name = data['tenant_name']
    domain_name = data['domain_name']
    prof = profile.Profile()
    prof.set_region(profile.Profile.ALL, region)
    return connection.Connection(
        profile=prof,
        user_agent='examples',
        auth_url=auth_url,
        username=username,
        password=password,
        project_name=tenant_name,
        region_name=region,
        project_domain_name=domain_name,
        user_domain_name=domain_name,
        identity_api_version=3,
        # identity_api_version=identity_api_version,
        # image_api_version=image_api_version)
        image_api_version=2)
def pythone_version():
    '''python版本兼容'''
    import sys
    data = show_openstack_connection_now()
    py_version = sys.version_info.major
    if py_version == 3:
        print('python3')
        return op_connectionv3(data)
    elif py_version == 2:
        print('python2')
        return op_connectionv2(data)
    else:
        print('没有找到python,请安装python')
