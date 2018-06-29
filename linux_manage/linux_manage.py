# -*- coding: utf-8 -*-
# author:xiaoming
import paramiko
auth={'root':['000000','123456']}
ssh_auth={'hostname':'172.24.2.11','username':'root','password':auth['root'][0]}
ssh=paramiko.SSHClient()
ssh.set_missing_host_key_policy(policy=paramiko.AutoAddPolicy)
ssh.connect(hostname=ssh_auth.get('hostname'),username=ssh_auth.get('username'),password=ssh_auth.get('password'))
stdin,stdout,stderr=ssh.exec_command('yum install xo*')
def read_try(obj):
    data=''
    try:
        data=obj.read().decode()
    except Exception as e:
        pass
    else:
        return data
stdin=read_try(stdin)
stdout=read_try(stdout)
stderr=read_try(stderr)
if stdin:
    print('input',stdin)
if stdout:
    print(stdout)
if stderr:
    print('error',stderr)
ssh.close()