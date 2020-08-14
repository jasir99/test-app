from .models import PropertyAddress,PropertyImage
from rest_framework import serializers

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyAddress
        fields = '__all__'
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = ('property', 'image')