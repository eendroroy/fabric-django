from fabric.operations import run

from config.fabric.create_paths import __create_paths
from config.fabric.create_symlinks import __create_symlinks
from config.fabric.tasks.restart_emperor import __task_restart_emperor
from config.fabric.tasks.restart_nginx import __task_restart_nginx
from config.fabric.upload_config import __upload_configs


def __task_setup():
    __create_paths()
    __upload_configs()
    __create_symlinks()
    run('sudo systemctl daemon-reload')
    __task_restart_nginx()
