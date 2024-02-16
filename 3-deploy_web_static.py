do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy


def deploy():
    """
    Deploys the web_static content to the web servers.
    """
    archive_path = do_pack()
    if not archive_path:
        return False
    return do_deploy(archive_path)
