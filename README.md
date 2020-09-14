# Websocket example based on Django-3.1
Implementing websocket without external dependency, no channel-redis, no dwebsocket.

inspired by following articles:

1. Jayden Windle - [How to Add Websockets to a Django App without Extra Dependencies](https://dev.to/jaydenwindle/adding-websockets-to-your-django-app-with-no-extra-dependencies-2f6h)
2. ArunRocks - [A Guide to ASGI in Django 3.0 and its Performance](https://arunrocks.com/a-guide-to-asgi-in-django-30-and-its-performance/#q-when-can-i-write-async-code-in-django)
3. Alex Oleshkevich - [WebSockets in Django 3.1](https://medium.com/@alex.oleshkevich/websockets-in-django-3-1-73de70c5c1ba)

4. [Coroutines and Tasks](https://docs.python.org/3/library/asyncio-task.html)

5. [Python并发之异步I/O(async,await)](https://www.jianshu.com/p/db2e5d222bb9)

----
## Highlight in this example
- Websocket with Django 3.1 without external dependences.
- Running project via ASGI (uvicorn) instead of WSGI
- Loading static files in ASGI mode
- Interactively sending and receiving message between server and client, no blocking in any task.
----
## Evironment Preparation
1. Python 3.7 or 3.8
2. Django 3.1
3. uviorn
4. ASGIMiddlewareStatic

```sh
python -m venv .venv # create virtual python environment
pip install django # install django > 3.1
pip install uvicorn  # install ASGI server
python manage.py collectstatic # generate static files
pip install -U ASGIMiddlewareStaticFile # install ASGIMiddlewareStatic
git clone https://github.com/stevechenzy/websocket-example-based-on-Django-3.1.git # download source code project to local
python manage.py collectstatic # generate static files
uvicorn project_name.asgi:application # run server
```
