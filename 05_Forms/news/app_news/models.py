from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.template.defaultfilters import truncatechars
from taggit.managers import TaggableManager


class News(models.Model):
    STATUS_CHOICES = [
        ('a', 'Active'),
        ('i', 'Inactive')
    ]
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=False)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='a')
    tag = TaggableManager()

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'
        permissions = (
            ('can_publish', 'Может опубликовать'),
        )

    def get_absolute_url(self):
        return reverse('newsdetail', args=[str(self.id)])

    def __str__(self):
        return f'{self.id}. {self.title}, {self.created_at}'


class Commentary(models.Model):
    STATUS_CHOICES = [
        ('p', 'Admin_pass'),
        ('d', 'Admin_delete')
    ]
    news_at = models.ForeignKey(News, related_name='comments', on_delete=models.CASCADE)
    user_name = models.CharField(max_length=20)
    comment = models.CharField(max_length=150)
    created_at = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='p')

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return f'Comment by {self.user_name} on {self.created_at}'

    @property
    def short_comment(self):
        return truncatechars(self.comment, 15)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=36, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)






