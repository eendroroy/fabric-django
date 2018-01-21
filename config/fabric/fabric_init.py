import datetime
from fabric.state import env
import os


def __fabric_init():
    env.deploy_key = f'/home/{env.user}/.ssh/{env.deploy_key_name}'

    env.directory = f'/home/{env.user}/apps/{env.app_name}'
    env.release_path = f'{env.directory}/releases'
    env.shared_path = f'{env.directory}/shared'
    env.current_path = f'{env.directory}/current'
    env.config_path = f'{env.shared_path}/config'
    env.source_path = f'{env.directory}/source'

    if env.pyenv == 'system':
        env.pyenv_root = '/usr/local/pyenv'
    else:
        env.pyenv_root = f'/home/{env.user}/.pyenv'

    env.pyenv_prefix = f'PYENV_ROOT={env.pyenv_root} PYENV_VERSION={env.pyenv_version} {env.pyenv_root}/bin/pyenv exec'

    env.venv = f'{env.shared_path}/venv'
    env.activate = f'source {env.shared_path}/venv/bin/activate'

    env.local_path = os.getcwd()
    env.release_name = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

    env.paths = [
        env.directory, env.shared_path, env.config_path
    ]

    env.uploads = []
    env.symlinks = []
