# -*- coding: utf-8 -*-
# author:xiaoming
from flask import Flask,request,render_template,jsonify,redirect
import json,os,sys
PATH=os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
filename='%s/%s'%(PATH,'op_connect')
from core.tools import file_write
from core import views
from core.libconn import op_lib_conn
openstack=views.openstack(op_lib_conn())
app=Flask(__name__)
@app.route('/help')
def help_list():
    return render_template('test.html')
@app.route('/')
def index():
    if request.method=='GET':
        return 'Welcome To Python OpenStack API'
@app.route('/v3',methods=['GET','POST'])
def op_v3():
    if request.method=='GET':
        return 'OpenStack V3 Auth'
@app.route('/connect',methods=['GET','POST'])
def op_conn():
    '''创建连接'''
    if request.method=='GET':
        form_list=['region_name','domain_name','auth_url','project_name','auth_username','auth_password']
        return render_template('form.html',action='/connect',data=form_list)
    elif request.method=='POST':
        data={
        'auth_username':request.values.get('auth_username'),
        'auth_url':request.values.get('auth_url'),
        'auth_password':request.values.get('auth_password'),
        'project_name':request.values.get('project_name'),
        'domain_name':request.values.get('domain_name'),
        'region_name':request.values.get('region_name'),
        }
        filename='%s/db/%s'%(PATH,'op_connect.json')
        file_write(filename,data)
        return redirect('/test/connect')
@app.route('/test/connect',methods=['GET'])
def test_conn():
    '''连接测试'''
    conn=op_lib_conn()
    if not conn:
        return jsonify({'error':'no set connect'})
    try:
        conn.list_images()
    except Exception as e:
        return jsonify({'error':'connection fail'})
    else:
        openstack.conn=op_lib_conn()
        return jsonify({'info':'ok'})
        # return 'ok'
@app.route('/v3/nova/create',methods=['GET','POST'])
def nova_create():
    if request.method=='GET':
        images=openstack.image_list()
        flavors=openstack.flavor_list()
        networks=openstack.network_list()
        return render_template('select.html',action='/v3/nova/create',images=images,flavors=flavors,networks=networks,name='name')
    elif request.method=='POST':
        name=request.values.get('name')
        image = request.values.get('image')
        flavor = request.values.get('flavor')
        network=request.values.get('network')
        data=openstack.nova_create(name,image,flavor,network)
        return jsonify(data)
        # return jsonify({'name':name,'image':image,'flavor':flavor})
@app.route('/v3/nova/<id>/<cmd>',methods=['GET'])
def cmd_obj(cmd,id):
    '''nova下的使用方法'''
    if id=='all':
        func = 'nova_%s_%s' %(cmd,id)
    else:
        func='nova_%s'%cmd
    if hasattr(openstack,func):
        obj=getattr(openstack,func)
        data=obj(id)
        return jsonify(data)
    else:
        return jsonify({'error':'no nova project'})
@app.route('/v3/<project>/list',methods=['GET'])
def list_obj(project):
    '''查看带有列表对象的信息'''
    func='%s_list'%(project)
    if hasattr(openstack,func):
        obj=getattr(openstack,func)
        data=obj(dict_json=True)
        return jsonify(data)
    else:
        return jsonify({'error':'no project list'})
@app.route('/v3/<project>/<id>',methods=['GET'])
def get_obj(project,id):
    '''查看带有id的对象的详细信息'''
    func = '%s_get' % (project)
    if hasattr(openstack, func):
        obj = getattr(openstack, func)
        data=obj(id,dict_json=True)
        return jsonify(data)
    return jsonify({'error':'No mode of submission'})
def image_create():
    pass