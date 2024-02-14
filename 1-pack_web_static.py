#!/usr/bin/python3
"""
Fabric script that generates a .tgz file from the contents of the web_static
"""

from fabric.api import local
from time import strftime

def do_pack():
    """
    Generates a .tgz file from the contents of the web_static
    """
    
    date = strftime("%Y%m%d%H%M%S")
    file_name = "versions/web_static_{}.tgz".format(date)
    try:
        local("mkdir -p versions")
        local(f"tar -zcvf {file_name} web_static")
    except Exception as err:
        return None