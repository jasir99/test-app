from django.contrib.auth.hashers import make_password

from rest_framework import serializers
from rest_framework.authtoken.serializers import AuthTokenSerializer

from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    # def create(self, validated_data):
    #     validated_data['password'] = make_password(validated_data['password'])
    #     client = User.objects.create(**validated_data)
    #     return client


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        user = User.objects.filter(username).first()
        return user
