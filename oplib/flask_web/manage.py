# -*- coding: utf-8 -*-
# author:xiaoming
def run():
    from flask_web.app.main.views import app
    app.run(host='0.0.0.0',port=8621,debug=True)
