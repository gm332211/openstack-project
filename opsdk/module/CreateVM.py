# -*- coding: utf-8 -*-
# author:xiaoming
    #服务器列表
class create_vm(object):
    def list_servers(conn):
        print("List Servers:")
        for server in conn.compute.servers():
            print(server)
    #镜像列表
    def list_images(conn):
        print("List Images:")
        for image in conn.compute.images():
            print(image)
    #flavors列表
    def list_flavors(conn):
        print("List Flavors:")
        for flavor in conn.compute.flavors():
            print(flavor)
    #网络列表
    def list_networks(conn):
        print("List Networks:")
        for network in conn.network.networks():
            print(network)
#秘钥对列表
def create_keypair(conn,SSH_DIR,KEYPAIR_NAME,PRIVATE_KEYPAIR_FILE):
    import os,errno
    keypair = conn.compute.find_keypair(KEYPAIR_NAME)
    if not keypair:
        print("Create Key Pair:")
        keypair = conn.compute.create_keypair(name=KEYPAIR_NAME)
        print(keypair)
        try:
            os.mkdir(SSH_DIR)
        except OSError as e:
            if e.errno != errno.EEXIST:
                raise e
        with open(PRIVATE_KEYPAIR_FILE, 'w') as f:
            f.write("%s" % keypair.private_key)
        os.chmod(PRIVATE_KEYPAIR_FILE, 0o400)
    return keypair
#创建服务器
def create_server(conn,IMAGE_NAME,FLAVOR_NAME,NETWORK_NAME,SERVER_NAME,PRIVATE_KEYPAIR_FILE):
    print("Create Server:")
    image = conn.compute.find_image(IMAGE_NAME)
    flavor = conn.compute.find_flavor(FLAVOR_NAME)
    network = conn.network.find_network(NETWORK_NAME)
    keypair = create_keypair(conn)
    server = conn.compute.create_server(
        name=SERVER_NAME, image_id=image.id, flavor_id=flavor.id,
        networks=[{"uuid": network.id}], key_name=keypair.name)
    server = conn.compute.wait_for_server(server)
    print("ssh -i {key} root@{ip}".format(
        key=PRIVATE_KEYPAIR_FILE,
        ip=server.access_ipv4))