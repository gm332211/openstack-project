# -*- coding: utf-8 -*-
# author:xiaoming
from flask import Flask,request,render_template,jsonify,redirect
import json,os,sys
PATH=os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
sys.path.insert(0,PATH)
filename='%s/%s'%(PATH,'op_connect')
from core.tools import file_write
from core import views
from core.libconn import op_lib_conn

app=Flask(__name__)
@app.route('/help')
def help_list():
    return render_template('test.html')
@app.route('/')
def index():
    if request.method=='GET':
        return 'This is index'
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
        print(filename)
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
        return jsonify({'info':'ok'})
        # return 'ok'
@app.route('/v3/nova/list',methods=['GET'])
def nova_list():
    conn=op_lib_conn()
    data=views.nova_list(conn)
    return jsonify(data)
@app.route('/v3/image/list',methods=['GET'])
def image_list():
    conn = op_lib_conn()
    data = views.image_list(conn)
    return jsonify(data)
