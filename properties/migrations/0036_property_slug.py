# Generated by Django 3.1.7 on 2021-07-28 12:21

import autoslug.fields
from django.db import migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0035_auto_20210718_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='slug',
            field=autoslug.fields.AutoSlugField(default=django.utils.timezone.now, editable=False, populate_from='title'),
            preserve_default=False,
        ),
    ]
