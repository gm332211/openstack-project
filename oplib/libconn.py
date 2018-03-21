# -*- coding: utf-8 -*-
# author:xiaoming
from libcloud.compute.providers import get_driver
from libcloud.compute.types import Provider
import os,sys
PATH=os.path.dirname(__file__)
sys.path.insert(0,PATH)
from tools import file_read
filename='%s/db/%s'%(PATH,'op_connect')
data=file_read(filename)
auth_username = data['auth_username']
auth_password = data['auth_password']
auth_url = data['auth_url']
project_name = data['project_name']
domain_name= data['domain_name']
region_name = data['region_name']
# auth_username = 'admin'
# auth_password = '000000'
# auth_url = 'http://%s:5000'%'controller'
# project_name = 'admin'
# domain_name='domain'
# region_name = 'RegionOne'
def op_lib_conn():
    provider = get_driver(Provider.OPENSTACK)
    return provider(auth_username,
                    auth_password,
                    ex_force_auth_url=auth_url,
                    ex_force_auth_version='3.x_password',
                    ex_tenant_name=project_name,
                    ex_domain_name=domain_name,
                    ex_force_service_region=region_name)

