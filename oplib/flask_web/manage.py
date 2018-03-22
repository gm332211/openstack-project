# -*- coding: utf-8 -*-
# author:xiaoming
# import os,sys
# PATH=os.path.dirname(os.path.dirname(__file__))
# sys.path.insert(0,PATH)
# print(PATH)
def run():
    from flask_web.app.main.views import app
    app.run(host='0.0.0.0',port=8621,debug=True)
