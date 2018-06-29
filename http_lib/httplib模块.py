# -*- coding: utf-8 -*-
# author:xiaoming
from http import client
import urllib
conn1=client.HTTPConnection('www.baidu.com:80')
print(conn1)
print(dir(conn1))
print(conn1.host)

conn1.request('GET','/','',{'user-agent':'test'})

res=conn1.getresponse()

body=res.read()
f=open('test.html','w',encoding='utf-8')
f.write(body.decode())
f.close()
conn1.close()
