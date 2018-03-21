# -*- coding: utf-8 -*-
# author:xiaoming
from flask import Flask
from flask import request
from flask import render_template
app=Flask(__name__)
@app.route('/',methods=['GET','POST'])
def home():
    return render_template('home.html')
@app.route('/signin',methods=['GET'])
def signin_form():
    return render_template('signin.html')
@app.route('/signin',methods=['POST'])
def signin():
    username=request.form['username']
    password=request.form['password']
    if username=='admin' and password=='password':
        return render_template('login-ok.html',username=username)
    return render_template('signin.html',message='bad username password',username=username)
app.run(host='0.0.0.0',port=8051,debug=True)