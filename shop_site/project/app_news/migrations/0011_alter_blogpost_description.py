# Generated by Django 3.2.16 on 2022-11-27 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_news', '0010_rename_post_blogpost_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='description',
            field=models.CharField(max_length=2000),
        ),
    ]
