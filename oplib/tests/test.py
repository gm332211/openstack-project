# -*- coding: utf-8 -*-
# author:xiaoming
# @openstack_api.route('/v3/<project>/<id>/<cmd>',methods=['GET'])
# def nova_del(project,id,cmd):
#     '''所有带id后的操作'''
#     func='%s_%s'%(project,cmd)
#     if hasattr(openstack_api,func):
#         obj=getattr(openstack_api,func)
#         data=obj(id)
#         return jsonify(data)
#     else:
#         return jsonify({'error': 'no project list'})
# @openstack_api.route('/v3/nova/<id>/reboot',methods=['GET'])
# def nova_reboot(id):
#     data=openstack_api.nova_reboot(id)
#     return jsonify(data)
# @openstack_api.route('/v3/nova/<id>/del',methods=['GET'])
# def nova_del(id):
#     data=openstack_api.nova_del(id)
#     return data
# @openstack_api.route('/v3/nova/<id>/reboot',methods=['GET'])
# def nova_reboot(id):
#     data=openstack_api.nova_reboot(id)
#     return jsonify(data)
# @openstack_api.route('/v3/nova/<id>/del',methods=['GET'])
# def nova_del(id):
#     data=openstack_api.nova_del(id)
#     return data
# @openstack_api.route('/v3/nova/all/reboot',methods=['GET'])
# def nova_reboot_all():
#     data=openstack_api.nova_reboot_all()
#     return jsonify(data)
# @openstack_api.route('/v3/nova/all/del',methods=['GET'])
# def nova_del_all():
#     data=openstack_api.nova_del_all()
#     return jsonify(data)