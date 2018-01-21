from fabric.context_managers import cd
from fabric.contrib.files import exists
from fabric.operations import run
from fabric.state import env

from config.fabric.venv import virtualenv


def task_deploy():
    if exists(env.source_path):
        with cd(env.source_path):
            run(f'exec ssh-agent bash -c "ssh-add {env.deploy_key} && git pull origin {env.branch}"')
            run(f'git checkout {env.branch}')
    else:
        run(f'exec ssh-agent bash -c "ssh-add {env.deploy_key} && git clone {env.project_url} {env.source_path}"')
        with cd(env.source_path):
            run(f'git checkout {env.branch}')

    with cd(env.source_path):
        run(f'mkdir -p {env.release_path}/{env.release_name}')
        run(f'git archive master | tar -x -C {env.release_path}/{env.release_name}')
        run(f'rm {env.current_path} || true')
        run(f'/bin/ln -nfs {env.release_path}/{env.release_name} {env.current_path}')

    with cd(env.current_path):
        with virtualenv():
            run(f'pip install -r {env.current_path}/requirements/prod.txt')
            run('sudo service emperor restart')
