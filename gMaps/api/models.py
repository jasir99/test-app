from django.db import models

class Address(models.Model):
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    street_number = models.CharField(max_length=20, null=True)
    zip_code = models.CharField(max_length=100, null=True)
    full_address = models.CharField(max_length=100)
    lattitude = models.FloatField()
    longitude = models.FloatField()
    latLong = models.CharField(max_length=20)