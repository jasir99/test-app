# Generated by Django 3.1 on 2020-08-11 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_address_administrative'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='administrative',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
