# -*- coding: utf-8 -*-
# author:xiaoming
import os,sys
PATH_BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,PATH_BASE)
from conf.setting import db_conf,help_dic
from db import db_orm
import os
class store_data(object):
    '''数据存储的类
    engine:存储的引擎
    link,db连接配置
    '''
    def __init__(self,engine,db_link,*args,**kwargs):
        self.engine=engine
        self.link=db_link
        self.args=args
        self.kwargs=kwargs
    def handle_engine(self):
        '''判断引擎'''
        if self.engine=='mysql':
            return self.__db_session()
        elif self.engine=='file':
            # return self.file_connection()
            pass
    def __db_session(self):
        '''连接数据库生成session'''
        from sqlalchemy import create_engine
        from sqlalchemy.orm import sessionmaker
        engine = create_engine(self.link, encoding='utf-8', echo=False)
        session_class = sessionmaker(bind=engine)
        session = session_class()
        return session
    def db_drop_table(self):
        '''初始化数据库'''
        from sqlalchemy import create_engine
        from sqlalchemy.ext.declarative import declarative_base
        Base=declarative_base()
        Base.metadata.drop_all(create_engine(self.link, encoding='utf-8'))
    def db_add(self,obj):
        '''添加表内容
        table_obj:表的对象'''
        session = self.__db_session()
        try:
            session.add(obj)
            session.commit()
        except Exception as e:
            print(e)
            return 0
    def del_data(self):
        '''删除数据'''
        pass
    def db_update(self):
        '''更新函数'''
        pass
    def db_select(self,table_name,*args,**kwargs):
        '''查询函数'''
        sess=self.__db_session()
        my_data = sess.query(db_orm.Endpoint).filter(db_orm.Endpoint.id == '1').first()
    def file_connection(self):
        if hasattr(self.kwargs,'filename'):
            pass
        else:
            print('缺少filename参数')
        pass
    def write_file(self,filename,*args,**kwargs):
        pass
class nova_class(object):
    '''openstacksdk调用函数类'''
    def create_keypair(self,conn,keypair_name,ssh_dir='private_key_dir',private_keypair_file='openstack-key'):
        '''创建虚机秘钥'''
        import os,errno
        keypair = conn.compute.find_keypair(keypair_name)
        if not keypair:
            print("Create Key Pair:")
            keypair = conn.compute.create_keypair(name=keypair_name)
            print(keypair)
            try:
                os.mkdir('%s\%s'%(PATH_BASE,ssh_dir))
            except OSError as e:
                if e.errno != errno.EEXIST:
                    raise e
            file_path='%s\%s\%s'%(PATH_BASE,ssh_dir,private_keypair_file)
            with open(file_path, 'w') as f:
                f.write("%s" % keypair.private_key)
            os.chmod(file_path, 0o400)
        return keypair
    def create_server(self,*args,**kwargs):
        '''创建虚拟机 :半成品'''
        from core.op_connect import pythone_version
        print(args[0])
        print(args)
        image_name = args[0][0]
        flavor_name = args[0][1]
        network_name = args[0][2]
        server_name = args[0][3]
        conn=pythone_version()
        keypair = self.create_keypair(conn=conn, keypair_name='openstack-key',
                                 ssh_dir='private_key_dir',
                                 private_keypair_file='openstack-key')
        private_keypair_file='openstack-key'
        print("Create Server:")
        image = conn.compute.find_image(image_name)
        flavor = conn.compute.find_flavor(flavor_name)
        network = conn.network.find_network(network_name)
        # keypair = create_keypair(conn)
        if private_keypair_file and keypair:
            server = conn.compute.create_server(
                name=server_name, image_id=image.id, flavor_id=flavor.id,
                networks=[{"uuid": network.id}], key_name=keypair.name)
        server = conn.compute.wait_for_server(server)
        print("ssh -i {key} root@{ip}".format(
            key=private_keypair_file,
            ip=server.access_ipv4))
        #vm写入数据库
        import datetime
        vm_obj=db_orm.Openstack_vm(name=server.name,vm_id=server.id,create_time=datetime.datetime.now())
        m1 = store_data(engine='mysql', db_link=db_conf['mysql'])
        m1.db_add(vm_obj)
        return server
nova_obj=nova_class()
from core import connect_set
from flask_web import flask_server
handle = {
    'mysql':{
    },
    'endpoint': {
        'create': connect_set.create_openstack_connection,
        'list':connect_set.list_openstack_connection,
        'set':connect_set.set_openstack_connection,
        'now':connect_set.echo_openstack_connection
    },
    'server':{
        'create':nova_obj.create_server
    },
    'flask':{
        'run':flask_server.run
    }
}