# project_name\project_name\asgi.py
"""
ASGI config for project_name project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

# to support static files
from asgi_middleware_static_file import ASGIMiddlewareStaticFile
from django.conf import settings
from django.core.asgi import get_asgi_application
from websocket.middleware import websockets

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_name.settings')

application = get_asgi_application()
application = websockets(application)
application = ASGIMiddlewareStaticFile(
    application, static_url=settings.STATIC_URL, static_paths=[settings.STATIC_ROOT]
)
