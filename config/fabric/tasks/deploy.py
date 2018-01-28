# -*- coding: future_fstrings -*-

from fabric.context_managers import cd
from fabric.contrib.files import exists
from fabric.operations import run
from fabric.state import env

from config.fabric.tasks.clean_releases import __task_clean_releases
from config.fabric.venv import __virtualenv


def __task_deploy():
    if exists(env.source_path):
        with cd(env.source_path):
            run(
                f'exec ssh-agent bash -c "ssh-add {env.deploy_key} && '
                f'git fetch origin +refs/heads/*:refs/heads/* --prune"'
            )
    else:
        run(
            f'exec ssh-agent bash -c "ssh-add {env.deploy_key} && '
            f'git clone --bare {env.project_url} {env.source_path}"'
        )

    with cd(env.source_path):
        run(f'mkdir -p {env.release_path}/{env.release_name}')
        run(f'git archive {env.branch} | tar -x -C {env.release_path}/{env.release_name}')
        run(f'rm {env.current_path} || true')
        run(f'/bin/ln -nfs {env.release_path}/{env.release_name} {env.current_path}')

    with cd(env.current_path):
        with __virtualenv():
            run(f'pip install -r {env.current_path}/requirements/prod.txt')
            run('sudo service emperor restart')

    __task_clean_releases()
