from fabric.operations import run


def __task_restart_emperor():
    run('sudo service emperor restart')
