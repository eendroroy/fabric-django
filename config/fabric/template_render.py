# -*- coding: future_fstrings -*-

from fabric.state import env
from jinja2 import Template


def __render_template(template_file):
    template = Template(open(template_file).read())

    return template.render(the='variables', env=env)
