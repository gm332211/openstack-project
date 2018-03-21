# -*- coding: utf-8 -*-
# author:xiaoming
#用户列表
def list_users(conn):
    print("List Users:")
    for user in conn.identity.users():
        print(user)
#凭证列表
def list_credentials(conn):
    print("List Credentials:")
    for credential in conn.identity.credentials():
        print(credential)
#项目列表
def list_projects(conn):
    print("List Projects:")
    for project in conn.identity.projects():
        print(project)
#域列表
def list_domains(conn):
    print("List Domains:")
    for domain in conn.identity.domains():
        print(domain)
#组列表
def list_groups(conn):
    print("List Groups:")
    for group in conn.identity.groups():
        print(group)
#服务列表
def list_services(conn):
    print("List Services:")
    for service in conn.identity.services():
        print(service)
#api列表
def list_endpoints(conn):
    print("List Endpoints:")
    for endpoint in conn.identity.endpoints():
        print(endpoint)
#区域列表
def list_regions(conn):
    print("List Regions:")
    for region in conn.identity.regions():
        print(region)