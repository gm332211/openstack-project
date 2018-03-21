# -*- coding: utf-8 -*-
# author:xiaoming
#创建一个秘钥
def create_secret(conn):
    print("Create a secret:")
    conn.key_manager.create_secret(name="My public key",
                                   secret_type="public",
                                   expiration="2020-02-28T23:59:59",
                                   payload="ssh rsa...",
                                   payload_content_type="text/plain")
#查看秘钥列表
def list_secrets(conn):
    print("List Secrets:")
    for secret in conn.key_manager.secrets():
        print(secret)
#详细查询
def list_secrets_query(conn):
    print("List Secrets:")
    for secret in conn.key_manager.secrets(
            secret_type="symmetric",
            expiration="gte:2020-01-01T00:00:00"):
        print(secret)
#获取秘钥
def get_secret_payload(conn,s):
    print("Get a secret's payload:")
    # Assuming you have an object `s` which you perhaps received from
    # a conn.key_manager.secrets() call...
    '''s=conn.key_manager.secrets()'''#获取秘钥的一个对象
    secret = conn.key_manager.get_secret(s.secret_id)
    print(secret.payload)
