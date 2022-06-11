from django.urls import path
from app.views import (
    ArticleAPIView,
    ArticleListView
)

urlpatterns = [
    path("articles/", ArticleListView.as_view(), name="article-list"),
    path("articles/request/", ArticleAPIView.as_view()),
]