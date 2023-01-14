from django.db import models
from django.urls import reverse


class Apartment(models.Model):
    address = models.CharField(verbose_name='адрес', max_length=100)
    name = models.CharField(verbose_name='название здания', max_length=100)

    class Meta:
        verbose_name = 'апартаменты'
        verbose_name_plural = 'апартаменты'

    def __str__(self):
        return f'{self.name}, {self.address}'


class RoomCount(models.Model):
    count = models.PositiveIntegerField(default=1, verbose_name='количество комнат')

    class Meta:
        verbose_name = 'количество комнат'
        verbose_name_plural = 'количество комнат'

    def __str__(self):
        return str(self.count)


class RoomType(models.Model):
    address = models.ForeignKey(Apartment, verbose_name='адрес', on_delete=models.CASCADE)
    room_type_choices = (
        ('Жилое', 'Жилое'),
        ('Рабочее', 'Рабочее')
    )
    room_type = models.CharField(choices=room_type_choices, max_length=10, verbose_name='тип помещения')
    room_count = models.ForeignKey(RoomCount, verbose_name='количество комнат', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'квартира'
        verbose_name_plural = 'квартиры'


class ApartmentNews(models.Model):
    title = models.CharField(verbose_name='заголовок', max_length=100, default='')
    short_description = models.CharField(verbose_name='краткое описание', max_length=100, default='')
    text = models.CharField(verbose_name='подробности', max_length=100, default='')
    published_at = models.DateTimeField(verbose_name='дата публикации', null=True)

    def get_absolute_url(self):
        return reverse('news_feed', args=[str(self.id)])

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'
