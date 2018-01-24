from fabric.operations import run
from fabric.state import env


def __task_clean_source():
    run(f'rm -rf {env.source_path}')
