#!/usr/bin/python3
"""
A Fabric script that distributes an archive to your web servers and deploys it.
"""

import os
from fabric.api import *
from fabric.operations import put, run, sudo
from datetime import datetime

env.hosts = ['54.237.2.254', '54.144.140.128']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


def do_pack():
    """Archives the static files."""
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    d_time = datetime.now()
    output = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        d_time.year,
        d_time.month,
        d_time.day,
        d_time.hour,
        d_time.minute,
        d_time.second
    )
    try:
        print("Packing web_static to {}".format(output))
        local("tar -cvzf {} web_static".format(output))
        size = os.stat(output).st_size
        print("web_static packed: {} -> {} Bytes".format(output, size))
    except Exception:
        output = None
    return output


def do_deploy(archive_path):
    """
    Distribute and deploy an archive to web servers.

    Args:
        archive_path (str): Path to the archive to deploy.

    Returns:
        bool: True if deployment succeeds, False otherwise.
	"""
    if os.path.exists(archive_path):
        return False
    try:
        put(archive_path, '/tmp/')

        archive_name = os.path.basename(archive_path)
        archive_base = archive_name.split(".")[0]

        release_dir = f"/data/web_static/releases/{archive_base}"
        current_dir = "/data/web_static/current"

        run(f"mkdir -p {release_dir}")
        run(f"tar -xzf /tmp/{archive_name} -C {release_dir}")

        run(f"rm /tmp/{archive_name}")

        run(f"mv {release_dir}/web_static/* {current_dir}")

        run(f"rm -rf {release_dir}")

        run(f"rm -rf {current_dir}")
        run(f"ln -s {release_dir} {current_dir}")

        print("New version deployed!")

        return True

    except Exception as e:
        print(f"Deployment failed: {e}")
        return False
    
