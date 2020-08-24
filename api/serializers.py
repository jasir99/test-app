from .models import PropertyAddress, PropertyImage, PropertyReview
from rest_framework import serializers

class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = '__all__'


class PropertyReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyReview
        fields = '__all__'


class PropertyAddressSerializer(serializers.ModelSerializer):
    images = PropertyImageSerializer(many=True, required=False)
    reviews = PropertyReviewSerializer(many=True, required=False)
    class Meta:
        model = PropertyAddress
        fields = ('id', 'city', 'country', 'property_description', 'full_address',
                  'latitude', 'longitude', 'images', 'reviews', 'user')