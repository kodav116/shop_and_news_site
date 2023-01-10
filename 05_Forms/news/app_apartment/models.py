from django.db import models


class Apartment(models.Model):
    address = models.CharField(verbose_name='адрес', max_length=100)
    name = models.CharField(verbose_name='название здания', max_length=100)

    class Meta:
        verbose_name = 'апартаменты'
        verbose_name_plural = 'апартаменты'


class RoomCount(models.Model):
    count = models.PositiveIntegerField(default=1)


class RoomType(models.Model):
    address = models.ForeignKey(Apartment, verbose_name='адрес', on_delete=models.CASCADE)
    room_type_choices = (
        (0, 'Жилое'),
        (1, 'Рабочее')
    )
    room_type = models.CharField(choices=room_type_choices, max_length=1)
    room_count = models.ForeignKey(RoomCount, verbose_name='количество комнат', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'квартира'
        verbose_name_plural = 'квартиры'


class ApartmentNews(models.Model):
    title = models.CharField(verbose_name='заголовок', max_length=100)
    short_description = models.CharField(verbose_name='краткое описание', max_length=100)
    text = models.CharField(verbose_name='подробности', max_length=100)

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'
