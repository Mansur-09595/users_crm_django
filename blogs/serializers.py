from rest_framework import serializers
from .models import Post

class UsersSerializer(serializers.ModelSerializer):
    
    class Meta:
        fields = ('full_name', 'time',  'category', )
        model = Post