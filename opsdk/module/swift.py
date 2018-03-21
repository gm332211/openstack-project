# -*- coding: utf-8 -*-
# author:xiaoming
#容器列表(特性:接收到<500 more Containers>)
def list_swfits(conn):
    for cont in conn.object_store.containers(limit=500):
        print(cont)
#创建容器
def create_swfit(conn):
    cont = conn.object_store.create_container(name="new container")
#查看容器信息
def info_swfit(conn):
    cont = conn.object_store.get_container_metadata("new container")
#修改其他用户访问容器的权限
def role_swift(conn):
    cont = conn.object_store.get_container_metadata("new container")
    cont.write_ACL = "big_project:another_user"
    conn.object_store.set_container_metadata(cont)
#查看容器内部信息
def show_swfit(conn):
    cont = conn.object_store.get_container_metadata("new container")
    for obj in conn.object_store.objects(cont):
        print(obj)
#显示最大条数
def max_show_swift(conn):
    for obj in conn.object_store.objects("pictures".decode("utf8"),limit=100):
        print(obj)
#获取对象内容
def get_data_swift(conn):
    cont = conn.object_store.get_container_metadata("new container")
    for obj in conn.object_store.objects(cont):
        print(obj)
        data = conn.object_store.get_object_data(obj)
        print(data)
#保存对象到磁盘
def download_data_swift(conn):
    cont = conn.object_store.get_container_metadata("new container")
    for obj in conn.object_store.objects(cont):
        print(obj)
        conn.object_store.download_object(obj, "the_message.txt")
def upload_data_swift(conn):
            conn.object_store.upload_object(container="messages",
                                            name="helloworld.txt",
                                            data="Hello, world!")
