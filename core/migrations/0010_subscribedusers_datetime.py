# Generated by Django 3.2.7 on 2022-04-01 10:01

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_subscribedusers'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscribedusers',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
