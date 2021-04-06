from rest_framework import serializers
from django.contrib.auth.models import User
from .models import USERTABLE, PERMISSION

# User Serializer
class Usertable_Serializer(serializers.ModelSerializer):
    class Meta:
        model = USERTABLE
        fields = '__all__'
        # fields = ('id', 'username', 'email')


# User Serializer
class Permission_Serializer(serializers.ModelSerializer):
    class Meta:
        model = PERMISSION
        fields = '__all__'
