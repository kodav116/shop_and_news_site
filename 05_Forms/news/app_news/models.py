from django.contrib.auth.models import User
from django.db import models
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
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('пользователь'), null=True, blank=True)
    balance = models.IntegerField(default=0, verbose_name=_('баланс'))
    BUYER_STATUS = (
        (0, 'Common'),
        (1, 'Preferred'),
        (2, 'VIP'),
    )
    status = models.CharField(max_length=1, choices=BUYER_STATUS, default=0)
    purchase_history = models.PositiveIntegerField(default=0, verbose_name=_('История покупок'))

    class Meta:
        verbose_name = _('кабинет пользователя')
        verbose_name_plural = _('кабинеты пользователей')
        ordering = ['user']

    def __str__(self):
        return self.user


class Shops(models.Model):
    name = models.CharField(max_length=100, verbose_name=_('название магазина'))

    class Meta:
        verbose_name = _('магазин')
        verbose_name_plural = _('магазины')

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name=_('название продукта'))
    shop = models.ForeignKey(Shops, on_delete=models.CASCADE, verbose_name=_('продавец'))
    price = models.FloatField(verbose_name=_('цена'))
    quantity = models.IntegerField(default=5, verbose_name=_('количество'))
    image = models.ImageField(null=True, blank=True, upload_to='files/', verbose_name=_('картинка'))
    sales = models.IntegerField(default=0, verbose_name=_('Продажи'))

    class Meta:
        verbose_name = _('продукт')
        verbose_name_plural = _('продукты')

    def __str__(self):
        return self.name


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


class ProductProxy(Product):
    class Meta:
        verbose_name, verbose_name_plural = "отчет", "отчеты"
        proxy = True








