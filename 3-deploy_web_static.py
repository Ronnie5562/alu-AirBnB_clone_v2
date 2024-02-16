#!/usr/bin/python3
import re
from time import strftime
from fabric.context_managers import cd
from fabric.api import env, put, run, sudo, local
from os.path import join, exists, splitext

do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy

env.hosts = ["54.242.215.110", "34.229.154.33"]
def deploy():
    """
    Deploys the web_static content to the web servers.
    """
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
