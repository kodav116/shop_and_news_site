# Generated by Django 3.2.16 on 2022-11-27 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0011_alter_blogpost_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='file',
            field=models.FileField(blank=True, upload_to='blog/files'),
        ),
    ]
