#!/usr/bin/python3
"""A module for Fabric script that generates a .tgz archive."""
import os
import datetime
from fabric.api import local, runs_once


@runs_once
def do_pack():
    """Archives the static files."""
    dest = "versions"
    git_repo = "https://github.com/Pasitik/AirBnB_clone_v2.git"
    if not os.path.isdir(dest):
        os.makedirs(dest)

    local(f"git clone {git_repo}")
    repo_name = git_repo.split("/")[-1]
    target = f"{repo_name}/web_static"
    now = datatime.datetime.now()
    try:
        local(f"tar -czf {dest}/web_static_{now.strftime('%Y%m%d%H%M%S')}.tgz -C {target} .")
        local(f"rm -rf {repo_name}")
        return os.path.join(destination_directory, archive_name)
    except Exception as e:
        print(f"Error creating archive: {e}")
        return None
         



