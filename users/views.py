# project_name\users\views.py
from django.views.generic.base import TemplateView
from websocket.connection import WebSocket
import asyncio

class IndexView(TemplateView):
    template_name = "index.html"
# async def websocket_view(socket):
#     await socket.accept()
#     await socket.send_text('hello')
#     await socket.close()
async def echo(socket:WebSocket):
    message = await socket.receive_text()
    await socket.send_text(message)
async def active_messsage(socket: WebSocket):
    for i in range(1, 2):
        await asyncio.sleep(10)
        await socket.send_text(f'Active Message: [{i}]')
    print("active routine exist")
async def websocket_view(socket: WebSocket):
    await socket.accept()
    while True:
        # message = await socket.receive_text()
        # await socket.send_text(message)
        await asyncio.gather(
            echo(socket),
            active_messsage(socket)
        )