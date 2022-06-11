from rest_framework import serializers
from .models import Article
 
class ArticleSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Article
        fields = ('id','title', 'body', 'status')