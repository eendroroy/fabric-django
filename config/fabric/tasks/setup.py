from fabric.operations import run

from config.fabric.create_paths import __create_paths
from config.fabric.create_symlinks import __create_symlinks
from config.fabric.upload_config import __upload_configs


def task_setup():
    __create_paths()
    __upload_configs()
    __create_symlinks()
    run('sudo systemctl daemon-reload')
    run('sudo service nginx restart')
    run('sudo service emperor restart')