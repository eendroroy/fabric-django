from fabric.state import env

from config.fabric.fabric_init import __fabric_init
from config.fabric.tasks.clean_releases import __task_clean_releases
from config.fabric.tasks.clean_source import __task_clean_source
from config.fabric.tasks.deploy import __task_deploy
from config.fabric.tasks.generate_sudoers import __task_generate_sudoers
from config.fabric.tasks.restart_emperor import __task_restart_emperor
from config.fabric.tasks.restart_nginx import __task_restart_nginx
from config.fabric.tasks.setup import __task_setup

env.project_url = 'git@github.com:deployer/django-app.git'
env.branch = 'master'
env.hosts = ['192.168.33.10']
env.app_port = '8000'
env.uwsgi_process = 4
env.uwsgi_threads = 2

env.user = 'deployer'
env.key_filename = '~/.ssh/id_rsa'
env.deploy_key_name = None

env.app_name = 'django-app'
env.requirements_file = 'requirements.txt'

env.socket = f'/tmp/{env.app_name}.sock'

env.pyenv = 'system'  # system or local
env.pyenv_version = '3.6.0'

env.keep_releases = 10

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


deploy = __task_deploy
setup = __task_setup
generate_sudoers = __task_generate_sudoers
clean_source = __task_clean_source
clean_releases = __task_clean_releases
restart_nginx = __task_restart_nginx
restart_emperor = __task_restart_emperor
