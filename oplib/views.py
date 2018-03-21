# -*- coding: utf-8 -*-
# author:xiaoming
from oplib import op_lib_conn
conn=op_lib_conn()
def image_list():#获取镜像列表
    images = conn.list_images()
    data={}
    for image in images:
        data[image.name] = image_format(image)
    return data
def image_get(image_id):#获取单个镜像
    image=conn.get_image(image_id)
    return image_format(image)
def image_format(image):#格式化image对象成为字典
    data = {
        'name': image.name,
        'uuid': image.uuid,
        'id': image.id,
        'extra': image.extra,
    }
    return data
def flavor_list():#获取风味列表
    flavors=conn.list_sizes()
    data={}
    for flavor in flavors:
        data[flavor.name] = flavor_format(flavor)
    return data
def flavor_get(flavor_id):#获取单个风味
    flavor=conn.ex_get_size(flavor_id)
    return flavor_format(flavor)
def flavor_format(flavor):#格式化风味
    data = {
        'name': flavor.name,
        'uuid': flavor.uuid,
        'id': flavor.id,
        'vcpu': flavor.vcpus,
        'ram': flavor.ram,
        'disk': flavor.disk,
        'ephemeral_disk': flavor.ephemeral_disk,
        'swap': flavor.swap,
        'extra': flavor.extra,
        'bandwidth': flavor.bandwidth,
        'price': flavor.price
    }
    return data
def nova_list():#获取实例列表
    vms=conn.list_nodes()
    data={}
    for vm in vms:
        data[vm.name]=nova_format(vm)
    return data
def nova_get(vm_id):
    pass
def nova_format(vm):
    data={
            'name':vm.name,
            'uuid':vm.uuid,
            'id':vm.id,
            'state':vm.state,
            'size': vm.size,
            'private_ips':vm.private_ips,
            'public_ips':vm.public_ips,
            'created_at':vm.created_at,
            'image':vm.image,
            'extra':vm.extra
        }
    return data
data=nova_list()
print(data)