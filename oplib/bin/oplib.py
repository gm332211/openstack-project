# -*- coding: utf-8 -*-
# author:xiaoming
import os,sys
PATH=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,PATH)
from flask_web import manage
manage.run()