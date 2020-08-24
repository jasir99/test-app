from django.contrib.auth.hashers import make_password

from rest_framework import serializers

from .models import User
from api.serializers import PropertyAddressSerializer

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        client = User.objects.create(**validated_data)
        return client



class UserSerializer(serializers.ModelSerializer):
    addresses = PropertyAddressSerializer(many=True, required=False)
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'phone_number', 'address1', 'address2', 'first_name', 'last_name', 'image', 'addresses')