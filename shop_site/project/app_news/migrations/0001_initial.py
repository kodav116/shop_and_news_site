# Generated by Django 3.2.16 on 2022-11-12 12:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=150)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('is_active', models.BooleanField(default=False)),
                ('status', models.CharField(choices=[('a', 'Active'), ('i', 'Inactive')], default='a', max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Commentary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(blank=True, max_length=20, null=True)),
                ('comment', models.CharField(max_length=150)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('status', models.CharField(choices=[('p', 'Admin_pass'), ('d', 'Admin_delete')], default='p', max_length=1)),
                ('news_at', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='app_news.news')),
                ('user', models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
    ]