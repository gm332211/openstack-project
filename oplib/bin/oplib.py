# -*- coding: utf-8 -*-
# author:xiaoming
import os,sys
PATH=os.path.dirname(os.path.dirname(__file__))
sys.path.insert(0,PATH)
print(PATH)
from flask_web import manage
manage.run()