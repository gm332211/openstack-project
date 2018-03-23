# -*- coding: utf-8 -*-
# author:xiaoming
# @app.route('/v3/<project>/<id>/<cmd>',methods=['GET'])
# def nova_del(project,id,cmd):
#     '''所有带id后的操作'''
#     func='%s_%s'%(project,cmd)
#     if hasattr(openstack,func):
#         obj=getattr(openstack,func)
#         data=obj(id)
#         return jsonify(data)
#     else:
#         return jsonify({'error': 'no project list'})
# @app.route('/v3/nova/<id>/reboot',methods=['GET'])
# def nova_reboot(id):
#     data=openstack.nova_reboot(id)
#     return jsonify(data)
# @app.route('/v3/nova/<id>/del',methods=['GET'])
# def nova_del(id):
#     data=openstack.nova_del(id)
#     return data
# @app.route('/v3/nova/<id>/reboot',methods=['GET'])
# def nova_reboot(id):
#     data=openstack.nova_reboot(id)
#     return jsonify(data)
# @app.route('/v3/nova/<id>/del',methods=['GET'])
# def nova_del(id):
#     data=openstack.nova_del(id)
#     return data
# @app.route('/v3/nova/all/reboot',methods=['GET'])
# def nova_reboot_all():
#     data=openstack.nova_reboot_all()
#     return jsonify(data)
# @app.route('/v3/nova/all/del',methods=['GET'])
# def nova_del_all():
#     data=openstack.nova_del_all()
#     return jsonify(data)