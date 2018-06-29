# -*- coding: utf-8 -*-
# author:xiaoming
from flask import Flask,request,render_template,jsonify,make_response
from conf.setting import help_dic
from core import connect_set
app=Flask(__name__)
@app.route('/openstack_api/api/v3.0',methods=['GET'])
def home(): #get主页
    return render_template('home.html')
@app.route('/test')
def test(): #get测试页面
    if request.method=='GET':
        return render_template('test.html')
    else:
        return 'ok'
@app.route('/login', methods = ['GET', 'POST'])
def login(): #get登入页面
    from .forms import LoginForm
    form = LoginForm()
    return render_template('login.html',form=form)
@app.route('/openstack_api/api/v3.0/endpoint/list',methods=['GET'])
def endpoint(): #get连接方式
    data=connect_set.list_openstack_connection()
    return jsonify(data)
@app.route('/openstack_api/api/v3.0/endpoint/create',methods=['GET'])
def endpoint_form(): #get创建连接列表
    list=['ip','region','auth_url','username','password','tenant_name','domain_name']
    return render_template('form.html',action='/openstack_api/api/v3.0/endpoint/create',data=list)
@app.route('/openstack_api/api/v3.0/endpoint/create',methods=['POST'])
def endpoint_write(): #post创建连接
    data=request.form
    connect_set.create_openstack_connection()
    return 'ok'
    # return render_template('form.html',action='action',)
@app.route('/openstack_api/api/v3.0/endpoint/set',methods=['POST'])
def endpoint_set(): #post设置当前的连接
    pass
@app.route('/openstack_api/api/v3.0/endpoint/now',methods=['GET'])
def endpoint_now(): #get返回当前连接
    pass
@app.route('/openstack_api/api/v3.0/endpoint/del',methods=['DELETE'])
def endpoint_del(): #delete删除一个连接
    pass
@app.route('/openstack_api/api/v3.0/server',methods=['GET'])
def server(): #server 主页
    return render_template('server.html',data='Server',dict=help_dic['server'])
@app.route('/openstack_api/api/v3.0/server/create',methods=['GET'])
def server_form():
    list = ['ip', 'region', 'auth_url', 'username', 'password', 'tenant_name', 'domain_name']
    return render_template('form.html',action='/openstack_api/api/v3.0/server/create',data=list)
@app.route('/openstack_api/api/v3.0/server/create',methods=['POST'])
def server_create_get():
    return jsonify(help_dic)
    # return render_template('server_create.html',dict=help_dic['server'])
@app.route('/openstack_api/api/v3.0/server/list',methods=['GET'])
def server_list_get():
    return jsonify(help_dic)
@app.route('/openstack_api/api/v3.0/server/del',methods=['DELETE'])
def server_create_post():
    pass
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error':'Not found'}),404)
def run(*args,**kwargs):
    app.run(host='0.0.0.0',port=8051,debug=True)
#自定义404返回json数据
