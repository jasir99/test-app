# Generated by Django 3.1 on 2020-08-25 21:44

from django.db import migrations
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200824_2159'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', user.models.UserManager()),
            ],
        ),
    ]
