# Generated by Django 4.2.4 on 2023-11-06 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='blog/django.png', upload_to='blog/'),
        ),
    ]
