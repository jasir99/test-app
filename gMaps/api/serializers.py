from .models import PropertyAddress,PropertyImage
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework import parsers
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = '__all__'


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    # user = serializers.ReadOnlyField(source='user.username')
    images = ImageSerializer(source='taskimage_set', many=True, read_only=True)
    class Meta:


        model = PropertyAddress
        fields = ('images','property_description')

    def create(self, validated_data):
        images_data = self.context.get('view').request.FILES
        property_description = PropertyAddress.objects.create(property_description=validated_data.get('title', 'no-title'),
                                   user_id=1)
        for image_data in images_data.values():
            PropertyImage.objects.create(property_description=property_description, image=image_data)
        return property_description