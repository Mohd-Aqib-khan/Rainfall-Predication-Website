# Generated by Django 3.2.7 on 2022-03-16 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_slider'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='img',
            field=models.ImageField(default='', upload_to='slider'),
        ),
    ]
