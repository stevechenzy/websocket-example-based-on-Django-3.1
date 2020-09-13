# project_name\websocket\asgi.py
from django.core.asgi import get_asgi_application
from websocket.middleware import websockets
application = get_asgi_application()
application = websockets(application)