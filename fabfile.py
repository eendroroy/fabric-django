from fabric.state import env

from config.fabric.fabric_init import __fabric_init
from config.fabric.tasks.deploy import task_deploy
from config.fabric.tasks.generate_sudoers import task_generate_sudoers
from config.fabric.tasks.setup import task_setup

# env.hosts = ['128.199.199.111']
# env.user = 'forge'

env.project_url = 'git@github.com:openhealthalgorithms/ohaApiDjango.git'
env.branch = 'master'
env.hosts = ['192.168.33.10']
env.app_port = '8000'
env.uwsgi_process = 4
env.uwsgi_threads = 2
env.user = 'deployer'
env.key_filename = '~/.ssh/id_rsa'
env.deploy_key_name = 'ohaApiDjango'
env.forward_agent = True

env.app_name = 'ohaApiDjango'

env.socket = f'/tmp/{env.app_name}.sock'

env.pyenv = 'system'  # system or local
env.pyenv_version = '3.6.0'

__fabric_init()

env.uploads = [
    [f'emperor.service', 'emperor.service'],
    [f'app.ini', f'{env.app_name}.ini'],
    [f'nginx.conf', f'{env.app_name}_nginx.conf'],
    [f'uwsgi_params', 'uwsgi_params'],
]

env.symlinks = [
    [f'emperor.service', '/etc/systemd/system/emperor.service'],
    [f'{env.app_name}_nginx.conf', f'/etc/nginx/sites-enabled/{env.app_name}_nginx.conf'],
    [f'uwsgi_params', '/etc/nginx/uwsgi_params'],
    [f'{env.app_name}.ini', f'/etc/uwsgi/apps-enabled/{env.app_name}.ini'],
]


def deploy(): task_deploy()


def setup(): task_setup()


def generate_sudoers(): task_generate_sudoers()
