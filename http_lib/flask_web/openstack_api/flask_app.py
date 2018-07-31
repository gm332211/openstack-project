
# -*- coding: utf-8 -*-
# author:xiaoming

from flask import Flask,jsonify,render_template,request,redirect,url_for
import op_handle
import json
from tools import file_write,file_read
from db.connect_db import Op_Connect, engine
from sqlalchemy.orm import sessionmaker
op_at_conn={
    'ip':None,
    'port':None,
    'domain':None,
    'project':None,
    'username':None,
    'password':None
}
app=Flask(__name__)
@app.route('/')
@app.route('/index')
def index():
    return "hello world!"
@app.route('/v3',methods=['GET'])
def openstack_v3():
    tittle='welcome to openstack_api api'
    form_tittle='create openstack_api connect'
    data_list=['ip','port','domain','project','username','password']
    return render_template('form.html',action='/v3',data=data_list,tittle=tittle,form_tittle=form_tittle)
@app.route('/v3',methods=['POST'])
def create_connect():
    #创建opesntack连接
    DBSession = sessionmaker(engine)
    session = DBSession()
    new_connect=Op_Connect(ip=request.values.get('ip'),
                           port=request.values.get('port'),
                           domain=request.values.get('domain'),
                           project=request.values.get('project'),
                           username=request.values.get('username'),
                           password=request.values.get('password'))
    session.add(new_connect)
    try:
        session.commit()
    except Exception:
        return redirect('/v3')
    session.close()
    return redirect('/v3/list')
@app.route('/v3/list',methods=['GET'])
def connect_list():
    #获取openstack连接列表
    from db.connect_db import Op_Connect, engine
    from sqlalchemy.orm import sessionmaker
    DBSession = sessionmaker(engine)
    session = DBSession()
    data_list=session.query(Op_Connect).all()
    try:
        connect=file_read('connect.json')
    except Exception:
        connect=None
    for data in data_list:
        print(data.id,data.ip,data.port,data.domain,data.project,data.username,data.password)
    id = request.values.get('id')
    req_status=request.values.get('status')
    status = ''
    if id:
        if req_status=='delete':
            status=connect_delete(id)
        elif req_status=='connect':
            status=connect_test(id)
        if not status:
            return redirect('/v3/list')
        else:
            return status
    return render_template('list.html',tittle_list=['id','ip','port','domain','project','username'],data=data_list,use_openstack=connect,status=status)
def db_query(id=None,db=Op_Connect):
    #db查询操作
    if id:
        DBSession = sessionmaker(engine)
        session = DBSession()
        try:
            data = session.query(Op_Connect).filter_by(id=id).first()
        except Exception:
            return None
        session.close()
        return data
    else:
        DBSession = sessionmaker(engine)
        session = DBSession()
        try:
            data = session.query(db).all()
        except Exception:
            return None
        session.close()
        return data
def connect_test(id):
    #测试openstack连接
    data=db_query(id)
    if data:
        op = op_handle.openstack(data.ip + ':' + data.port,
                                 username=data.username,
                                 domain=data.domain,
                                 password=data.password,
                                 project=data.project)
        res = op.get_token()
        if res == '':
            return '连接失败'
        data_dic={'ip': data.ip,
                   'port': data.port,
                   'domain': data.domain,
                   'project': data.project,
                   'username': data.username,
                   'password': data.password}
        file_write('connect.json', data_dic)
        return '连接成功'
    return '连接失败'
def connect_delete(id=None,db=Op_Connect):
    data = db_query(id,db)
    if data:
        DBSession=sessionmaker(engine)
        session=DBSession()
        try:
            session.delete(data)
            session.commit()
        except Exception:
            return '删除失败'
        return '删除成功'
    else:
        return '删除失败'
@app.route('/v3/<project>',methods=['GET'])
def identity_list(project):
    #认证的所有对象的列表
    try:
        connect = file_read('connect.json')
    except Exception as e:
        return
    op=op_handle.openstack(connect['ip']+':'+connect['port'],
                           username=connect['username'],
                           domain=connect['domain'],
                           password=connect['password'],
                           project=connect['project'])
    project=op.op_request('GET','/v3/%s'%project)
    data=project.read().decode()
    data_json=json.loads(data)
    return jsonify(data_json)
@app.route('/v3/<project>/<id>',methods=['GET'])
# 获取单个认证对象的详细信息
def identity_show(project,id):
    connect = file_read('connect.json')
    op = op_handle.openstack(connect['ip'] + ':' + connect['port'],
                             username=connect['username'],
                             domain=connect['domain'],
                             password=connect['password'],
                             project=connect['project'])
    project = op.op_request('GET','/v3/%s/%s'%(project,id))
    data=project.read().decode()
    data_json=json.loads(data)
    return jsonify(data_json)
@app.route('/v3/<project>',methods=['POST'])
# 创建一个认证对象
def identity_create(project):

    pass
# @app.route('v3/<project>/<id>',methods=['delete'])
#删除一个认证对象
def identity_delete(project,id):
    pass
@app.route('/v2.1/<project>')
def compute_list(project):

    pass
@app.route('/v2.1/<project>/<id>')
def compute_show(project,id):
    pass
app.run(debug=True,threaded=True)
