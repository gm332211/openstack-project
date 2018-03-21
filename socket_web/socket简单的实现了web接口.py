# -*- coding: utf-8 -*-
# author:xiaoming
import socket
def handle_request(client):
    data=client.recv(1024)
    print(data)
    msg='HTTP/1.1 200 OK\r\n\r\n'
    client.send(('%s'%msg).encode())
    msg='hello world!'
    client.send(('%s'%msg).encode())
def run():
    server=socket.socket()
    server.bind(('localhost',8082))
    server.listen(5)
    while True:
        cnn,addr=server.accept()
        handle_request(cnn)
        cnn.close()
if __name__ == '__main__':
    run()