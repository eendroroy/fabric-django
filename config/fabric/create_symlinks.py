# -*- coding: future_fstrings -*-

from fabric.operations import run
from fabric.state import env


def __create_symlinks():
    for link in env.symlinks:
        run(f'sudo /bin/ln -nfs {env.shared_path}/config/{link[0]} {link[1]}')
