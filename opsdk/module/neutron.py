# -*- coding: utf-8 -*-
# author:xiaoming
#网络列表
def list_networks(conn):
    print("List Networks:")
    for network in conn.network.networks():
        print(network)
#子网列表
def list_subnets(conn):
    print("List Subnets:")
    for subnet in conn.network.subnets():
        print(subnet)
#端口列表
def list_ports(conn):
    print("List Ports:")
    for port in conn.network.ports():
        print(port)
#安全组列表
def list_security_groups(conn):
    print("List Security Groups:")
    for port in conn.network.security_groups():
        print(port)
#路由列表
def list_routers(conn):
    print("List Routers:")
    for router in conn.network.routers():
        print(router)
#网络代理列表
def list_network_agents(conn):
    print("List Network Agents:")
    for agent in conn.network.agents():
        print(agent)
#创建网络
def create_network(conn):
    print("Create Network:")
    example_network = conn.network.create_network(
        name='openstacksdk-example-project-network')
    print(example_network)
    example_subnet = conn.network.create_subnet(
        name='openstacksdk-example-project-subnet',
        network_id=example_network.id,
        ip_version='4',
        cidr='10.0.2.0/24',
        gateway_ip='10.0.2.1')
    print(example_subnet)
#安全组设置端口访问
def open_port(conn):
    print("Open a port:")
    example_sec_group = conn.network.create_security_group(
        name='openstacksdk-example-security-group')
    print(example_sec_group)
    example_rule = conn.network.create_security_group_rule(
        security_group_id=example_sec_group.id,
        direction='ingress',
        remote_ip_prefix='0.0.0.0/0',
        protocol='HTTPS',
        port_range_max='443',
        port_range_min='443',
        ethertype='IPv4')
    print(example_rule)
#创建icmp规则
def allow_ping(conn):
    print("Allow pings:")
    example_sec_group = conn.network.create_security_group(
        name='openstacksdk-example-security-group2')
    print(example_sec_group)
    example_rule = conn.network.create_security_group_rule(
        security_group_id=example_sec_group.id,
        direction='ingress',
        remote_ip_prefix='0.0.0.0/0',
        protocol='icmp',
        port_range_max=None,
        port_range_min=None,
        ethertype='IPv4')
    print(example_rule)
#删除网络
def delete_network(conn):
    print("Delete Network:")
    example_network = conn.network.find_network(
        'openstacksdk-example-project-network')
    for example_subnet in example_network.subnet_ids:
        conn.network.delete_subnet(example_subnet, ignore_missing=False)
    conn.network.delete_network(example_network, ignore_missing=False)