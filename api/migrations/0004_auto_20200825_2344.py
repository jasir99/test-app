# Generated by Django 3.1 on 2020-08-25 21:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0003_auto_20200824_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertyaddress',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='properties', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='propertyreview',
            name='propertyAddress',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='api.propertyaddress'),
        ),
        migrations.AlterField(
            model_name='propertyreview',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL),
        ),
    ]
