from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login

from rest_framework import serializers

from .models import User
from api.serializers import PropertyAddressSerializer
from api.models import PropertyAddress


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        client = User.objects.create(**validated_data)
        return client


class UserSerializer(serializers.ModelSerializer):
    properties = PropertyAddressSerializer(many=True, required=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'phone_number', 'address1', 'address2', 'first_name', 'last_name', 'image',
                  'properties')


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        user = authenticate(username=username, password=password)

        if user is None:
            raise serializers.ValidationError('A user with this email and password is not found.')
        try:
            queryset = PropertyAddress.objects.filter(user=user.pk)
            properties_serializer = PropertyAddressSerializer(queryset, many=True)
            update_last_login(None, user)
        except:
            raise serializers.ValidationError('Wrong credentials')
        return {
            'user': user,
            'properties': properties_serializer.data
        }

