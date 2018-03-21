# -*- coding: utf-8 -*-
# author:xiaoming
#查看策略类型
def list_policy_types(conn):
    print("List Policy Types:")
    for pt in conn.cluster.policy_types():
        print(pt.to_dict())
#获得策略类型
def get_policy_type(conn):
    print("Get Policy Type:")
    pt = conn.cluster.get_policy_type('senlin.policy.deletion-1.0')
    print(pt.to_dict())
#检查策略
def list_policies(conn):
    print("List Policies:")
    for policy in conn.cluster.policies():
        print(policy.to_dict())
    for policy in conn.cluster.policies(sort='name:asc'):
        print(policy.to_dict())
#创建策略
def create_policy(conn):
    print("Create Policy:")
    spec = {
        'policy': 'senlin.policy.deletion',
        'version': 1.0,
        'properties': {
            'criteria': 'oldest_first',
            'destroy_after_deletion': True,
        }
    }
    policy = conn.cluster.create_policy('dp01', spec)
    print(policy.to_dict())
#查找策略
def find_policy(conn):
    print("Find Policy:")
    policy = conn.cluster.find_policy('dp01')
    print(policy.to_dict())
#获取策略名称或者id
def get_policy(conn):
    print("Get Policy:")
    policy = conn.cluster.get_policy('dp01')
    print(policy.to_dict())
#更新策略
def update_policy(conn):
    print("Update Policy:")
    policy = conn.cluster.update_policy('dp01', name='dp02')
    print(policy.to_dict())
#删除策略
def delete_policy(conn):
    print("Delete Policy:")
    conn.cluster.delete_policy('dp01')
    print("Policy deleted.")