# project_name/urls.py
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from users import views
from websocket.urls import websocket

urlpatterns = [
    path("", views.IndexView.as_view()),
    websocket("ws/", views.websocket_view),
]
urlpatterns += staticfiles_urlpatterns()
