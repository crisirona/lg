"""
WSGI config for pj_auto project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os, sys

project_home = '/home/crissirona'

if project_home not in sys.path:
    sys.path.insert(0,project_home)

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pj_auto.settings')

application = get_wsgi_application()

