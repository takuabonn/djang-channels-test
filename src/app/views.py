from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics

from .models import Article
from app.serializers import ArticleSerializer
from .consumers import ArticleConsumer
import time


# Create your views here.
class ArticleAPIView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        articleSerializer = ArticleSerializer(data={"title":data["title"], "body": data["body"], "status": "request"})
        articleSerializer.is_valid()
        articleSerializer.save()
        savedArticle = articleSerializer.data

        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            'article', 
            {
                "type": "comminucateStatus",
                "message": {'id': savedArticle['id'], 'status': savedArticle['status']}
            }
        )

        time.sleep(30)

        aproveTargetArticle = Article.objects.get(id=savedArticle['id'])
        aprovedArticleSerializer = ArticleSerializer(aproveTargetArticle, data={"title":data["title"], "body": data["body"], "status": "aproved"}, partial=True)
        aprovedArticleSerializer.is_valid()
        aprovedArticleSerializer.save()
        aprovedArticel = aprovedArticleSerializer.data

        async_to_sync(channel_layer.group_send)(
            'article', 
            {
                "type": "comminucateStatus",
                "message": {'id': aprovedArticel['id'], 'status': aprovedArticel['status']}
            }
        )
        content = {'sucsess': 'ok'}
        return Response(content, status=status.HTTP_201_CREATED)


class ArticleListView(generics.ListAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        return Article.objects.order_by('id').reverse().all()




        

        

