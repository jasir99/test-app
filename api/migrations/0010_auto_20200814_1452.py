# Generated by Django 3.1 on 2020-08-14 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_propertyaddress_autocomplete_address'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='propertyaddress',
            unique_together={('latitude', 'longitude')},
        ),
    ]
