# Generated by Django 3.1.7 on 2021-07-08 04:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0032_auto_20210708_0343'),
    ]

    operations = [
        migrations.AddField(
            model_name='lovedproperties',
            name='lovedate',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
