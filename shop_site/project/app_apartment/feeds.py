from django.contrib.syndication.views import Feed
from django.db.models import QuerySet
from django.urls import reverse
from app_apartment.models import ApartmentNews


class ApartmentNewsFeed(Feed):
    title = 'Новости'
    link = '/sitenews/'
    description = 'Новости о жилье'

    def items(self) -> QuerySet:
        return ApartmentNews.objects.order_by('-published_at')[:5]

    def item_title(self, item: ApartmentNews) -> str:
        return item.title

    def item_description(self, item: ApartmentNews) -> str:
        return item.text

    def item_link(self, item: ApartmentNews) -> str:
        return reverse('news_feed', args=[item.pk])