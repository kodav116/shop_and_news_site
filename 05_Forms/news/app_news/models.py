from django.contrib.auth.models import User
from django.db import models
from django import forms
from django.urls import reverse
from django.template.defaultfilters import truncatechars
from django.utils.translation import gettext_lazy as _


class News(models.Model):
    STATUS_CHOICES = [
        ('a', 'Active'),
        ('i', 'Inactive')
    ]
    title = models.CharField(max_length=50, verbose_name=_('название'))
    description = models.CharField(max_length=150, verbose_name=_('тело'))
    created_at = models.DateField(auto_now_add=True, verbose_name=_('дата создания'))
    updated_at = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=False, verbose_name=_('активность'))
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='a')

    class Meta:
        verbose_name = _('новость')
        verbose_name_plural = _('новости')
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
    news_at = models.ForeignKey(News, related_name='comments', on_delete=models.CASCADE, verbose_name=_('новость'))
    user_name = models.CharField(max_length=20, verbose_name=_('имя'))
    comment = models.CharField(max_length=150, verbose_name=_('тело'))
    created_at = models.DateField(auto_now_add=True, verbose_name=_('дата создания'))
    active = models.BooleanField(default=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='p')

    class Meta:
        verbose_name = _('комментарий')
        verbose_name_plural = _('комментарии')
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


class BlogImage(models.Model):
    file = models.FileField()


class BlogPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('пользователь'))
    description = models.CharField(max_length=2000, verbose_name=_('пост'))
    created_at = models.DateField(auto_now_add=True)
    file = models.ManyToManyField(BlogImage, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _('профиль')
        verbose_name_plural = _('профили')
        ordering = ['created_at']

    @property
    def short_post(self):
        return truncatechars(self.description, 100)


class Offers(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('пользователь'))
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    discounts = models.CharField(max_length=500, verbose_name=_('скидки'), blank=True)
    specials = models.CharField(max_length=500, verbose_name=_('предложения'), blank=True)
    history = models.CharField(max_length=500, verbose_name=_('история'), blank=True)
    shops = models.CharField(max_length=500, verbose_name=_('магазины'), blank=True)

    class Meta:
        verbose_name = _('программа лояльности')
        verbose_name_plural = _('программы лояльности')
        ordering = ['user']


class Author(models.Model):
    name = models.CharField(max_length=30, verbose_name=_('имя'))
    surname = models.CharField(max_length=30, verbose_name=_('фамилия'))
    birth_year = models.DateField(verbose_name=_('год рождения'))

    class Meta:
        verbose_name = _('автор')
        verbose_name_plural = _('авторы')


class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name=_('название'))
    isbn = models.IntegerField(max_length=13, verbose_name='ISBN')
    release_year = models.DateField(verbose_name=_('дата выпуска'))
    page_amount = models.IntegerField(verbose_name=_('количество страниц'))

    class Meta:
        verbose_name = _('книга')
        verbose_name_plural = _('книги')









