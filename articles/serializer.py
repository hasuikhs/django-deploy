from rest_framework import serializers
from .models import Article, Comment

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.ImageField()
    class Meta:
        model = Article
        fields = ('height', 'weight', 'image', 'fat', 'secret', 'title', 'content', 'created_at', 'updated_at', 'user', 'like_users')

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('article', 'user', 'content', 'created_at', 'updated_at')