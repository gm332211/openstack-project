# -*- coding: utf-8 -*-
# author:xiaoming
#文件类型列表
def list_profile_types(conn):
    print("List Profile Types:")
    for pt in conn.cluster.profile_types():
        print(pt.to_dict())
#得到文件类型
def get_profile_type(conn):
    print("Get Profile Type:")
    pt = conn.cluster.get_profile_type('os.nova.server-1.0')
    print(pt.to_dict())
#检查配置文件列表
def list_profiles(conn):
    print("List Profiles:")
    for profile in conn.cluster.profiles():
        print(profile.to_dict())
    for profile in conn.cluster.profiles(sort='name:asc'):
        print(profile.to_dict())
#创建一个想要的配置文件

def create_profile(conn):
    SERVER_NAME, FLAVOR_NAME, IMAGE_NAME, NETWORK_NAME = 0
    print("Create Profile:")
    spec = {
        'profile': 'os.nova.server',
        'version': 1.0,
        'properties': {
            'name': SERVER_NAME,
            'flavor': FLAVOR_NAME,
            'image': IMAGE_NAME,
            'networks': {
                'network': NETWORK_NAME
            }
        }
    }
    profile = conn.cluster.create_profile('os_server', spec)
    print(profile.to_dict())
#查找配置文件
def find_profile(conn):
    print("Find Profile:")
    profile = conn.cluster.find_profile('os_server')
    print(profile.to_dict())
#获取配置文件
def get_profile(conn):
    print("Get Profile:")
    profile = conn.cluster.get_profile('os_server')
    print(profile.to_dict())
#更新配置文件
def update_profile(conn):
    print("Update Profile:")
    profile = conn.cluster.update_profile('os_server', name='old_server')
    print(profile.to_dict())
#删除配置文件
def delete_profile(conn):
    print("Delete Profile:")
    conn.cluster.delete_profile('os_server')
    print("Profile deleted.")