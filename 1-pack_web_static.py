#!/usr/bin/python3
"""
Fabric script that generates a .tgz file from the contents of the web_static
"""
from fabric.api import local
from time import strftime


def do_pack():
    """ Generates a .tgz file from the contents of the web_static
    """

    date_time = strftime("%Y%m%d%H%M%S")
    file_name = f"versions/web_static_{date_time}.tgz"
    try:
        local("mkdir -p versions")
        local(f"tar -zcvf {file_name} web_static")
        return file_name
    except Exception as err:
        return None
