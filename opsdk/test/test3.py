# -*- coding: utf-8 -*-
# author:xiaoming
data = {
    'region': 'RegionOne',
    'auth_url': 'http://controller:35357/v3',
    'username': 'admin',
    'password': '000000',
    'tenant_name': 'admin',
    'domain_name': 'domain'
}
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
def list_users(conn):
    print("List Users:")
    for user in conn.identity.users():
        print(user)
conn=op_connectionv3(data)
list_users(conn)

