# -*- coding: future_fstrings -*-

from fabric.operations import run
from fabric.state import env


def __create_paths():
    for path in env.paths:
        run(f'mkdir -p {path}')
