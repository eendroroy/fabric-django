import tempfile

from fabric.operations import put
from fabric.state import env

from config.fabric.template_render import __render_template


def __upload_configs():
    for config in env.uploads:
        temp_file_path = f'{tempfile.gettempdir()}/{config[0]}'
        temp_file = open(temp_file_path, 'w+')
        temp_file.write(__render_template(f'{env.local_path}/config/deploy/templates/{config[0]}.j2'))
        temp_file.close()
        put(temp_file_path, f'{env.shared_path}/config/{config[1]}')
