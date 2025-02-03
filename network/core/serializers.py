from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.username')
    date_formatada = serializers.DateTimeField(source='created_date', format="%d/%m/%Y %H:%M")

    class Meta:
        model = Post
        fields = '__all__'