from rest_framework import serializers
from .models import Post

class UsersSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = ('first_name', 'last_name', 'age', 'author', 'post_date',)
        model = Post