"""
WSGI config for django_game_server project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os
import manage

from django.core.wsgi import get_wsgi_application

# check whether the log dir is exits
manage.check_log()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_game_server.settings")

application = get_wsgi_application()
