#!/usr/bin/python3
"""A module for Fabric script that generates a .tgz archive."""
import os
import datetime
from fabric.api import local, runs_once


@runs_once
def do_pack():
    """Archives the static files."""
    dest = "versions"
    script_directory = os.path.dirname(os.path.abspath(__file__))
    git_repo = "https://github.com/Pasitik/AirBnB_clone_v2.git"
    if not os.path.isdir(dest):
        os.makedirs(dest)

    local(f"git clone {git_repo}")
    repo_name = git_repo.split("/")[-1]
    new_name = repo_name.split(".")[-2]
    target = f"{new_name}/web_static"
    now = datetime.datetime.now()
    archive_name = f"web_static_{now.strftime('%Y%m%d%H%M%S')}.tgz"
    try:
        local(f"tar -czf {dest}/{archive_name} -C {target} .")
        local(f"rm -rf {new_name}")
        return os.path.join(dest, archive_name)
    except Exception as e:
        print(f"Error creating archive: {e}")
        return None
         



