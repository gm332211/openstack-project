# -*- coding: utf-8 -*-
# author:xiaoming
from flask import Flask,request,render_template,jsonify,make_response,redirect
import json,os,sys
PATH=os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
sys.path.insert(0,PATH)
filename='%s/%s'%(PATH,'op_connect')
from tools import file_write
import views
app=Flask(__name__)
@app.route('/')
def index():
    if request.method=='GET':
        return 'This is index'
app.run(host='0.0.0.0',port=8563,debug=True)
@app.route('/connect',methods=['GET','POST'])
def op_conn():
    '''创建连接'''
    if request.method=='GET':
        return render_template('form.html')
    elif request.method=='POST':
        data={
        'auth_username':request.values.get('auth_username'),
        'auth_url':request.values.get('auth_url'),
        'project_name':request.values.get('project_name'),
        'domain_name':request.values.get('domain_name'),
        'region_name':request.values.get('region_name'),
        }
        filename='%s/db/%s'%(PATH,'op_connect')
        file_write(filename,data)
        return redirect('/test/connect')
@app.route('/test/connect',methods=['GET'])
def test_conn():
    '''测试连接'''
    return 'ok'
@app.route('/v3/nova/list',methods=['GET'])
def nova_list():
    data=views.nova_list()
    return jsonify(data)