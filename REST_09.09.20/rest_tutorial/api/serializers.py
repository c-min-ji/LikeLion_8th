from rest_framework import serializers
from .models import Post

#PostSerializer 아니고 ApiSerializer
class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'pub_date', 'body')