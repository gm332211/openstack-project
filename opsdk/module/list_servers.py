from openstack import connection,profile,session
def create_connection(region, auth_url, username, password, project_name, domain_name, identity_api_version, image_api_version):
    prof = profile.Profile()
    prof.set_region(profile.Profile.ALL, region)
    print(region)
    return connection.Connection(
        profile=prof,
        user_agent='examples',
        auth_url=auth_url,
        username=username,
        password=password,
        project_name=project_name,
        region_name=region,
        project_domain_name=domain_name,
        user_domain_name=domain_name,
        identity_api_version=identity_api_version,
        image_api_version=image_api_version)
nova_link={
    'region':'RegionOne',
    'auth_url':'http://192.168.2.10:35357',
    'username':'admin',
    'password':'000000',
    'project_name':'admin',
    'domain_name':'000000',
    'identity_api_version':'3',
    'image_api_version':'2'
}

conn=create_connection(**nova_link)
for i in conn.compute.servers():
    print(i)
    print(dir(i))
for user in conn.identity.users():
    print(user)
