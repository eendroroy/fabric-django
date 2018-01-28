# -*- coding: future_fstrings -*-

from fabric.context_managers import cd
from fabric.operations import run
from fabric.state import env


def __task_clean_releases():
    with cd(env.release_path):
        releases = env.get("keep_releases") or 5
        releases_count = int(releases) if str(releases).isdigit() else 5
        run(f'rm -rf `ls -t | tail -n +{releases_count + 1}`')
