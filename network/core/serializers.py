from rest_framework import serializers
from .models import Post, Like
import json

class PostSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.username')
    date_formatada = serializers.DateTimeField(source='created_date', format="%d/%m/%Y %H:%M")
    likes_num = serializers.SerializerMethodField()
    liked = serializers.SerializerMethodField()

    def get_likes_num(self, obj):
        likes = Like.objects.filter(post=obj)
        return len(likes)

    def get_liked(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(post=obj, user=user)
            if like.exists():
                return True
        return False
    

    class Meta:
        model = Post
        fields = '__all__'