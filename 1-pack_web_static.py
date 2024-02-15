#!/usr/bin/python3
from fabric.api import local
from time import strftime


def do_pack():
    """
    Generates a .tgz file from the contents of the web_static folder
    
    Returns:
        str: The file path of the generated .tgz file if successful else None.
    """

    # date_time = strftime("%Y%m%d%H%M%S")
    # file_name = f"versions/web_static_{date_time}.tgz"
    # try:
    #     local("mkdir -p versions")
    #     local(f"tar -zcvf {file_name} web_static")
    #     return file_name
    # except Exception as err:
    #     return None
    
    pass
