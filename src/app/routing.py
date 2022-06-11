# from django.urls import re_path
from django.conf.urls import url

from app.consumers.ArticleConsumer import *

websocket_urlpatterns = [
    url(r'ws/article/', ArticleConsumer.as_asgi()),
]