# -*- coding: utf-8 -*-
# author:xiaoming
from wsgiref.simple_server import make_server
def handle_request(env,res): #env 所有http请求信息 res发送http响应函数
    res('200 OK',[('Content-Type','text/html')]) #生成http响应头 (200 Ok)HTTP响应码
    body='<h1>hello world</h1>' #生成http主体部分
    for i in env:
        print(i)
    return [body.encode()]
if __name__ == '__main__':
    http=make_server('127.0.0.1',8083,handle_request)
    print('Serving http on prot 8083')
    http.serve_forever()