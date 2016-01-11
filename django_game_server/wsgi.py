# coding=utf-8
"""
WSGI config for django_game_server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
import manage
from uwsgidecorators import timer
from django.core.wsgi import get_wsgi_application
from django.utils import autoreload
# The uWSGI server automagically adds a uwsgi module into your Python apps.
# http://uwsgi-docs.readthedocs.org/en/latest/PythonModule.html
import uwsgi

# check whether the log dir is exits
manage.check_log()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_game_server.settings")

application = get_wsgi_application()


# 发现代码发生变化自动热重启
@timer(3)
def change_code_gracefully_reload(sig):
    if autoreload.code_changed():
        uwsgi.reload()
