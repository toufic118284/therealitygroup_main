# Generated by Django 3.1.7 on 2021-06-28 15:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0025_auto_20210628_2043'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='gallery_images',
        ),
    ]