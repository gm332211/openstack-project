# -*- coding: utf-8 -*-
# author:xiaoming
import os,sys
PATH_BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,PATH_BASE)
if __name__ == '__main__':
    from core import main
    main.run()
