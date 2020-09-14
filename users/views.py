# project_name\users\views.py
import asyncio

from django.views.generic.base import TemplateView
from websocket.connection import WebSocket

round = 0

class IndexView(TemplateView):
    template_name = "index.html"
async def echo(socket:WebSocket):
    while True:
        message = await socket.receive_text()
        message = 'ECHO: ' + message
        await socket.send_text(message)
        
async def active_messsage(socket: WebSocket):
    global round
    while True:
        await asyncio.sleep(5)
        await socket.send_text(f'Active Message: [{round}]')
        round += 1

async def websocket_view(socket: WebSocket):
    await socket.accept()
    while True:
        await asyncio.gather(
            echo(socket),
            active_messsage(socket)
        )
