# -*- coding: future_fstrings -*-

from contextlib import contextmanager as _contextmanager

from fabric.context_managers import cd, prefix
from fabric.operations import run
from fabric.state import env


@_contextmanager
def __virtualenv():
    run(f'[ -d {env.venv} ] && true || {env.pyenv_prefix} virtualenv {env.venv}')
    with cd(env.directory):
        with prefix(env.activate):
            yield
