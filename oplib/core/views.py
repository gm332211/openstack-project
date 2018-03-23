# -*- coding: utf-8 -*-
# author:xiaoming
# from . import op_lib_conn
def try_obj(message=''):
    '''
    测试装饰器
        :param message: message_info type(dict)
        :return dict
    '''
    def try_out(func):
        def try_int(*args,**kwargs):
            try:
                rc=func(*args,**kwargs)
            except Exception as e:
                return message or {'error':'nothing id'}
            return rc
        return try_int
    return try_out
class openstack():
    '''
    apache libcloud二次封装类
        :param conn: apache libcloud connect
    '''
    def __init__(self,conn):
        self.conn=conn
    @try_obj()
    def image_get(self,image_id,dict_json=False,*args,**kwargs):
        '''
        获取单个镜像
            :param image_id: 镜像id type(str)
            :return dict_json False return obj True retrun dict
        '''
        image=self.conn.get_image(image_id)
        if dict_json:
            return image_format(image)
        return image
    @try_obj(message={'error':'Without this flavor id'})
    def flavor_get(self,flavor_id,dict_json=False,*args,**kwargs):
        '''
        获取单个风味
            :param flavor_id: 风味id type(str)
            :return dict_json False return obj True retrun dict
        '''
        flavor=self.conn.ex_get_size(flavor_id)
        if dict_json:
            return flavor_format(flavor)
        return flavor
    @try_obj(message={'error':'Without this network id'})
    def network_get(self,network_id,dict_json=False,*args,**kwargs):#获取单个网络
        networks = self.conn.ex_list_networks()
        for network in networks:
            if hasattr(network, 'id'):
                if getattr(network,'id') == network_id:
                    if dict_json:
                        return network_format(network)
                    return network
            else:
                return {'error':'no network id'}
        return {'error':'no find'}
    @try_obj()
    def nova_get(self,vm_id,dict_json=False,*args,**kwargs):#获取单个实例
        vms=self.conn.list_nodes()
        for vm in vms:
            if hasattr(vm,'id'):
                if getattr(vm,'id')==vm_id:
                    if dict_json:
                        return nova_format(vm)
                    return vm
            else:
                return {'error': 'no vm id'}
        return {'error': 'no find'}
    def nova_reboot(self,vm,*args,**kwargs):
        '''重启一个虚机'''
        if self.conn.reboot_node(vm):
            return {'info':'reboot success'}
        else:
            return {'error':'reboot fail'}
    def nova_reboot_many(self,vms,*args,**kwargs):
        '''重启多个虚机'''
        data={}
        for vm in vms:
            data[vm.name]=self.nova_reboot(vm)
        return data
    def flavor_list(self,*args,**kwargs):
        '''
        获取风味列表对象
            :return dict
        '''
        flavors=self.conn.list_sizes()
        data={}
        for flavor in flavors:
            data[flavor.name] = flavor_format(flavor)
        return data
    def image_list(self,*args,**kwargs):
        '''
        获取镜像列表对象
            :return dict
        '''
        images = self.conn.list_images()
        data={}
        for image in images:
            data[image.name] = image_format(image)
        return data
    def network_list(self,*args,**kwargs):
        '''
        获取网络列表对象
            :return dict
        '''
        networks=self.conn.ex_list_networks()
        data={}
        for network in networks:
            data[network.name]=network_format(network)
        return data
    def nova_list(self,dict_json=False,*args,**kwargs):#获取实例列表对象
        vms=self.conn.list_nodes()
        if dict_json:
            data={}
            for vm in vms:
                data[vm.name]=nova_format(vm)
            return data
        return vms
    def nova_create(self,name,image,size,network_id,ex_userdata='',*args,**kwargs):#创建虚拟机
        node=self.conn.create_node(name=name,
                                   image=self.image_get(image),
                                   size=self.flavor_get(size),
                                   networks=[self.network_get(network_id),],
                                   )
        return nova_format(node)
#一下都是格式化输出
def image_format(image):#格式化image对象成为字典
    data = {
        'name': image.name,
        'uuid': image.uuid,
        'id': image.id,
        'extra': image.extra,
    }
    return data
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
def network_format(network):
    data = {
        'name': network.name,
        'id':network.id,
        'cidr':network.cidr,
        'extra':network.extra
    }
    return data
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



