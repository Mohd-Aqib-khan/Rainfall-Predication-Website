# Generated by Django 3.2.7 on 2022-03-16 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('img', models.ImageField(default='', upload_to='myimage')),
                ('desc', models.CharField(max_length=200)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
