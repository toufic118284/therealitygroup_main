# Generated by Django 3.1.7 on 2021-06-25 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0013_remove_property_price_us'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='price_us',
            field=models.IntegerField(max_length=250, null=True),
        ),
    ]
