from django.contrib.sitemaps import Sitemap
from app_apartment.models import ApartmentNews


class NewsSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return ApartmentNews.objects.all()

    def lastmod(self, obj: ApartmentNews):
        return obj.published_at

