from django.db import models


class Advertisement(models.Model):
    title = models.CharField(max_length=1000, db_index=True)
    description = models.CharField(max_length=1000, default='', verbose_name='описание')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    price = models.FloatField(verbose_name='цена', default=0)
    views_count = models.IntegerField(verbose_name='количество просмотров', default=0)
    status = models.ForeignKey('AdvertisementStatus', default=None, null=True, on_delete=models.CASCADE,
                               related_name='advertisements')
    type = models.ForeignKey('AdvertisementType', default=None, null=True, on_delete=models.CASCADE,
                             related_name='advertisements')
    author = models.ForeignKey('Author', default=None, null=True, on_delete=models.CASCADE,
                               related_name='advertisements')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'advertisements'
        ordering = ['title']


class Author(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='имя')
    email = models.CharField(max_length=100, verbose_name='почта')
    phone = models.CharField(max_length=11, verbose_name='телефон')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'authors'
        ordering = ['name']


class AdvertisementType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class AdvertisementStatus(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
