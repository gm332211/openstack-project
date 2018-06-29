# -*- coding: utf-8 -*-
# author:xiaoming
'''openstack_api 连接endpoint的设置文件'''
from core.views import store_data
from core.tools import help_list,out_beautiful
from db import db_orm
from conf.setting import db_conf
import os
PATH_BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
m1 = store_data(engine='mysql', db_link=db_conf['mysql'])
sess = m1.handle_engine()
def create_openstack_connection(*args,**kwargs):
    '''创建openstack连接数据到mysql中 :已完成'''
    print(args[0])
    if len(args):
        ip=args[0][0]
        region=args[0][1]
        auth_url=args[0][2]
        username=args[0][3]
        password=args[0][4]
        tenant_name=args[0][5]
        domain_name=args[0][6]
    elif len(kwargs):
        ip=kwargs['ip']
        region=kwargs['region']
        auth_url=kwargs['auth_url']
        username=kwargs['username']
        password=kwargs['password']
        tenant_name=kwargs['tenant_name']
        domain_name=kwargs['domain_name']
    else:
        exit('请输入参数')
    user_obj = db_orm.User(
        username=username,
        password=password,
        tenant_name=tenant_name,
        domain_name=domain_name,
    )
    back = m1.db_add(user_obj)
    if not back:
        user_obj=sess.query(db_orm.User).filter(db_orm.User.username==username).filter(db_orm.User.tenant_name==tenant_name).filter(db_orm.User.domain_name==domain_name).first()
    endpoint_obj = db_orm.Endpoint(
        ip=ip,
        auth_url=auth_url,
        region=region,
        user_id=user_obj.id
    )
    m1.db_add(endpoint_obj)
def list_openstack_connection(*args,**kwargs):
    '''显示mysql中现有的openstack连接 :已完成'''
    # m1 = store_data(engine='mysql', db_link=db_conf['mysql'])
    # sess = m1.handle_engine()
    obj_list = sess.query(db_orm.Endpoint).all()
    data={}
    for obj in obj_list:
        print('-------%s-------'%(obj.id))
        print('id:%s\nip:%s\nauth_url:%s\nregion:%s\nusername:%s\ntenant_name:%s\ndomain_name:%s'%(
            obj.id,obj.ip,obj.auth_url,obj.region,obj.user.username,obj.user.tenant_name,obj.user.domain_name
        ))
        data[obj.id]={'ip':obj.ip,'auth_url':obj.auth_url,'region':obj.region,'username':obj.user.username}
    return data
def set_openstack_connection(*args,**kwargs):
    '''设置当前的openstack连接 :已完成'''
    # m1 = store_data(engine='mysql', db_link=db_conf['mysql'])
    # sess = m1.handle_engine()
    import os, json
    file_name = 'connection_conf.json'
    file_path = '%s\%s\%s' % (PATH_BASE, 'db', file_name)
    id=args[0][0]
    if os.path.exists(file_path):
        os.remove(file_path)
    try:
        endpoint = sess.query(db_orm.Endpoint).filter(db_orm.Endpoint.id == id).first()
    except Exception as e:
        print('参数错误',e)
        help_list()
    data={'ip':endpoint.ip,'region':endpoint.region,
          'auth_url':endpoint.auth_url,'username':endpoint.user.username,
        'password':endpoint.user.password,'tenant_name':endpoint.user.tenant_name,
          'domain_name':endpoint.user.domain_name}
    f=open(file_path,'w')
    json.dump(data,f)
    f.close()
    out_beautiful('设置成功')
    for i in data:
        print('%s: %s'%(i,data[i]))
def show_openstack_connection_now(*args,**kwargs):
    '''查看获取现在的openstack连接 :已完成'''
    import os, json
    file_name = 'connection_conf.json'
    file_path = '%s\%s\%s' % (PATH_BASE, 'db', file_name)
    if os.path.exists(file_path):
        f=open(file_path,'r')
        try:
            data=json.load(f)
        except Exception as e:
            out_beautiful('当前文件遭到破坏,请重新设置connection')
            help_list()
        f.close()
        if not f:
            out_beautiful('openstack连接配置设置出现问题请重新设置')
            help_list()
        else:
            return data
    else:
        out_beautiful('没有设置当前openstack连接配置')
        help_list()
def echo_openstack_connection(*args,**kwargs):
    data=show_openstack_connection_now()
    out_beautiful('当前连接的openstack认证')
    for i in data:
        print('%s: %s' % (i, data[i]))
def update_openstack_connection(*args,**kwargs):
    pass
