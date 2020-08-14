from django.db import models

class PropertyAddress(models.Model):
    property_description = models.CharField(max_length=3000, null=True)
    country = models.CharField(max_length=100)
    administrative_area_level_1 = models.CharField(max_length=100, null=True)
    administrative_area_level_2 = models.CharField(max_length=100, null=True)
    administrative_area_level_3 = models.CharField(max_length=100, null=True)
    administrative_area_level_4 = models.CharField(max_length=100, null=True)
    administrative_area_level_5 = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    street_number = models.CharField(max_length=20, null=True)
    zip_code = models.CharField(max_length=100, null=True)
    full_address = models.CharField(max_length=250)
    lattitude = models.FloatField()
    longitude = models.FloatField()
    latLong = models.CharField(max_length=20)

    def save(self, *args, **kwargs):
        super(PropertyAddress, self).save(*args, **kwargs)

class PropertyImage(models.Model):
    property = models.ForeignKey(PropertyAddress,related_name = 'images',on_delete=models.CASCADE)
    image = models.ImageField() 
    
    def __str__(self):
        return self.image