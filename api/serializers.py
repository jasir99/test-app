from .models import PropertyAddress, PropertyImage
from rest_framework import serializers

class PropertyAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyAddress
        fields = '__all__'

class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = '__all__'

class PropertyAddressSerializerWithImages(serializers.ModelSerializer):
    images = PropertyImageSerializer(many=True, required=False)
    class Meta:
        model = PropertyAddress
        fields = ('id', 'street_number', 'street', 'city', 'administrative_area_level_1',
                  'administrative_area_level_2', 'administrative_area_level_3', 'administrative_area_level_4',
                  'administrative_area_level_5', 'country', 'property_description', 'zip_code', 'full_address',
                  'autocomplete_address', 'latitude', 'longitude', 'latLong', 'images')