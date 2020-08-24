from django.db import models
from user.models import User


class PropertyAddress(models.Model):
    property_description = models.CharField(max_length=3000, null=True)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    full_address = models.CharField(max_length=250)
    latitude = models.FloatField()
    longitude = models.FloatField()
    user = models.ForeignKey(User, related_name='user_id', on_delete=models.CASCADE)

    class Meta:
        unique_together = (('latitude', 'longitude'),)


class PropertyImage(models.Model):
    propertyAddress = models.ForeignKey(PropertyAddress, default=None, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='property_images')


class PropertyReview(models.Model):
    content = models.CharField(verbose_name='content', max_length=2000)
    rating = models.PositiveSmallIntegerField(verbose_name='rating')
    propertyAddress = models.ForeignKey(PropertyAddress, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)

    class Meta:
        unique_together = (('propertyAddress', 'user'))