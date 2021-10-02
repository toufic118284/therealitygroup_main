# Generated by Django 3.1.7 on 2021-05-28 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Basic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_title', models.CharField(max_length=50)),
                ('logo', models.ImageField(upload_to='site_pic')),
                ('favicon', models.ImageField(upload_to='site_pic')),
                ('logo_link', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=25)),
                ('phone_link', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=25)),
                ('email_link', models.CharField(max_length=50)),
                ('facebook_link', models.CharField(max_length=50)),
                ('twitter_link', models.CharField(max_length=50)),
                ('footer_logo', models.ImageField(upload_to='site_pic')),
                ('footer_description', models.CharField(max_length=400)),
                ('footer_about_title', models.CharField(max_length=50)),
                ('footer_about', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background_image', models.ImageField(upload_to='slider_images')),
                ('title_top', models.CharField(max_length=220, null=True)),
                ('title', models.CharField(max_length=300, null=True)),
                ('description', models.TextField(null=True)),
                ('button_text', models.CharField(max_length=50, null=True)),
                ('button_url', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
