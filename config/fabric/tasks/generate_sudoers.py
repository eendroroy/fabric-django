from fabric.operations import local
from fabric.state import env

from config.fabric.template_render import __render_template


def __task_generate_sudoers():
    local(f'mkdir -p {env.local_path}/tmp/sudoer/')
    sudoer_file_path = f'{env.local_path}/tmp/sudoer/{env.user}'
    sudoer_file = open(sudoer_file_path, 'w+')
    sudoer_file.write(__render_template(f'{env.local_path}/config/deploy/templates/sudoer.j2'))
    sudoer_file.close()

    print(f' ==> {sudoer_file_path}')
