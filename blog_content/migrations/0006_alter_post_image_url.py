# Generated by Django 4.2.6 on 2024-09-24 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_content', '0005_rename_content_comment_poster_comment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_url',
            field=models.ImageField(blank=True, help_text='Upload an image', null=True, upload_to='images/'),
        ),
    ]
