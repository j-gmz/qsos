from .models import CustomUser
from rest_framework import serializers

class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser 
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]
