# -*- coding: utf-8 -*-
# author:xiaoming
#镜像列表
def list_images(conn):
    print("List Images:")
    for image in conn.image.images():
        print(image)
#创建镜像
def upload_image(conn,EXAMPLE_IMAGE_NAME):
    print("Upload Image:")
    # Load fake image data for the example.
    data = 'This is fake image data.'
    # Build the image attributes and upload the image.
    image_attrs = {
        'name': EXAMPLE_IMAGE_NAME,
        'data': data,
        'disk_format': 'raw',
        'container_format': 'bare',
        'visibility': 'public',
    }
    conn.image.upload_image(**image_attrs)
#MD5加密下载镜像
def download_image_stream(conn):
    print("Download Image via streaming:")
    # Find the image you would like to download.
    image = conn.image.find_image("myimage")
    # As the actual download now takes place outside of the library
    # and in your own code, you are now responsible for checking
    # the integrity of the data. Create an MD5 has to be computed
    # after all of the data has been consumed.
    import hashlib
    md5 = hashlib.md5()
    with open("myimage.qcow2", "wb") as local_image:
        response = conn.image.download_image(image, stream=True)
        # Read only 1024 bytes of memory at a time until
        # all of the image data has been consumed.
        for chunk in response.iter_content(chunk_size=1024):
            # With each chunk, add it to the hash to be computed.
            md5.update(chunk)
            local_image.write(chunk)
        # Now that you've consumed all of the data the response gave you,
        # ensure that the checksums of what the server offered and
        # what you downloaded are the same.
        if response.headers["Content-MD5"] != md5.hexdigest():
            raise Exception("Checksum mismatch in downloaded content")
#下载镜像
def download_image(conn):
    print("Download Image:")
    # Find the image you would like to download.
    image = conn.image.find_image("myimage")
    with open("myimage.qcow2", "w") as local_image:
        response = conn.image.download_image(image)
        # Response will contain the entire contents of the Image.
        local_image.write(response)
#删除一个镜像
def delete_image(conn):
    print("Delete Image:")
    example_image = conn.image.find_image(EXAMPLE_IMAGE_NAME)
    conn.image.delete_image(example_image, ignore_missing=False)