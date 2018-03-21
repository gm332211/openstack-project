# -*- coding: utf-8 -*-
# author:xiaoming
db_conf={
    'mysql':'mysql+pymysql://root:000000@localhost/testdb',
    'file':'C:/'
}
help_dic = {
    'mysql':{
    },
    'endpoint': {
        'create': '[ip][region][auth_url][username][password][tenant_name][domain_name]',
        'list':'',
        'set':'[endpoint_id]',
        'now':''
    },
    'server':{
        'create':'[image_name][flavor_name][network_name][server_name]'
    },
    'flask':{
        'run':''
    }
}