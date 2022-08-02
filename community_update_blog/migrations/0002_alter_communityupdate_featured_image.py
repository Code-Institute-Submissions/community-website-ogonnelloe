# Generated by Django 4.0.6 on 2022-08-02 00:05

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community_update_blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communityupdate',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(default='placeholder.jpg', max_length=255, verbose_name='image'),
        ),
    ]
