# project_name/urls.py
from django.urls import path
from websocket.urls import websocket
from users import views
urlpatterns = [
    path("", views.IndexView.as_view()),
    websocket("ws/", views.websocket_view),
]