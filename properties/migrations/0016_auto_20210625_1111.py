# Generated by Django 3.1.7 on 2021-06-25 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0015_auto_20210625_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='baths',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='beds',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='floor_size_ft2',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='floor_size_m2',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='floors',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='lot_Size_ft2',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='lot_Size_m2',
            field=models.IntegerField(null=True),
        ),
    ]
