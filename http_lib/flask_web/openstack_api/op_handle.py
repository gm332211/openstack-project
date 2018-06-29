# -*- coding: utf-8 -*-
# author:xiaoming
from http import client
import urllib
from urllib import request,response,parse
import json
from db.connect_db import Op_Connect, engine
from sqlalchemy.orm import sessionmaker
from tools import file_write,file_read
# data=parse.urlencode(json.dumps(auth)) #字符串的传递
class openstack(object):
    def __init__(self,host,username,password,project,domain):
        self.host=host
        self.username=username
        self.password=password
        self.project=project
        self.domain=domain
        self.op_at_conn={
            'ip': None,
            'port': None,
            'domain': None,
            'project': None,
            'username': None,
            'password': None
        }
    def get_token(self):
        #创建token
        auth = {
            "auth": {
                "identity": {
                    "methods": [
                        "password"
                    ],
                    "password": {
                        "user": {
                            "name": self.username,
                            "password": self.password,
                            "domain":{"name":self.domain}
                        }
                    }
                },
                "scope": {
                    "project": {
                        "name": self.project,
                        "domain":{"name":self.domain}
                    }
                }
            }
        }
        data = json.dumps(auth)  # json数据的传递
        headers = {
            "Content-type": "application/json"
        }
        try:
            conn = client.HTTPConnection(self.host)
        except Exception as e:
            print(e)
            return ''
        conn.request('POST', '/v3/auth/tokens', body=data, headers=headers)
        try:
            res = conn.getresponse()
        except Exception as e:
            return ''
        if res.status != 201:
            conn.close()
            return ''
        else:
            conn.close()
            return res.getheader('X-Subject-Token')
    def op_request(self,method,url,body=None):
        #处理请求
        token=self.get_token()
        headers={"Content-type": "application/json","X-Auth-Token":token}
        conn=client.HTTPConnection(self.host)
        conn.request(method=method,url=url,headers=headers,body=body)
        res=conn.getresponse()
        return res

class op_handles(object):
    def __init__(self):
        self.op_at_conn={
            'ip': None,
            'port': None,
            'domain': None,
            'project': None,
            'username': None,
            'password': None
        }
    def default_conn(self):
        data=file_read('connect.json')
        if data:
            op = openstack(data.ip + ':' + data.port,
                                     username=data.username,
                                     domain=data.domain,
                                     password=data.password,
                                     project=data.project)
            res = op.get_token()
            if res == '':
                return '连接失败'
            self.op_at_conn = data
            return '默认配置连接成功'
    def connect_test(self,id):
        # 测试openstack连接
        DBSession = sessionmaker(engine)
        session = DBSession()
        data = session.query(Op_Connect).filter_by(id=id).first()
        if data:
            op = openstack(data.ip + ':' + data.port,
                                     username=data.username,
                                     domain=data.domain,
                                     password=data.password,
                                     project=data.project)
            res = op.get_token()
            print(res)
            if res == '':
                return '连接失败'
            data_list = {
                'ip': data.ip,
                'port': data.port,
                'domain': data.domain,
                'project': data.project,
                'username': data.username,
                'password': data.password
            }
            self.op_at_conn=data_list
            file_write('connect.json', data_list)
            return '连接成功'
            # return '连接成功当前连接地址为%s:%s'%(data.ip,data.port)
        else:
            return '连接失败'





# op=openstack_api('172.30.14.8:5000',username='admin',domain='xiandian',password='z9wQNJRVHqpX5HfWKSBL',project='admin')
# users=op.op_request('GET','/v3/users')
# project=op.op_request('GET','/v3/projects')
# print(users.read().decode())
# print(project.read().decode())


# print(res.status)  # 状态信息
# print(res.version)  # 版本信息
# print(res.read().decode())  # 返回的主体
# print(res.reason)
# print(res.getheader('X-Subject-Token'))  # 获取头部信息


