# Generated by Django 3.1 on 2020-08-14 04:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20200813_1754'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Address',
            new_name='PropertyAddress',
        ),
        migrations.CreateModel(
            name='PropertyImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='api.propertyaddress')),
            ],
        ),
    ]