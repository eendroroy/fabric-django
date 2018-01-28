from fabric.operations import run


def __task_restart_nginx():
    run('sudo service nginx restart')
