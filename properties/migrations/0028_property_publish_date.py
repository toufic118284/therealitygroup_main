# Generated by Django 3.1.7 on 2021-07-01 03:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0027_auto_20210629_2300'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='publish_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
