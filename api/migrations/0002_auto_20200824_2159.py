# Generated by Django 3.1 on 2020-08-24 19:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='propertyaddress',
            name='user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_id', to='user.user'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='PropertyReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=2000, verbose_name='content')),
                ('rating', models.PositiveSmallIntegerField(verbose_name='rating')),
                ('address_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property', to='api.propertyaddress')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('address_id', 'user_id')},
            },
        ),
    ]
