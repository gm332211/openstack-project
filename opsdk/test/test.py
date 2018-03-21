# -*- coding: utf-8 -*-
# author:xiaoming
from openstack import connection
class test(object):
    data={
        'region':'RegionOne',
        'auth_url':'http://controller:35357/v3',
        'username':'admin',
        'password':'000000',
        'tenant_name':'admin',
        'domain_name':'domain'
    }
    def openstack_conn(self):
        region = data['region']
        auth_url = data['auth_url']
        username = data['username']
        password = data['password']
        tenant_name = data['tenant_name']
        domain_name = data['domain_name']
        conn=connection.Connection(
                        region_name=region,
                        auth=dict(
                            auth_url=auth_url,
                            username=username,
                            password=password,
                            project_name=tenant_name,
                            user_domain_name=domain_name),
                        compute_api_version='2',
                        identity_api_version=3,
                        identity_interface='internal')
    def list_users(conn):
        print("List Users:")
        for user in conn.identity.users():
            print(user)
list_users(conn)