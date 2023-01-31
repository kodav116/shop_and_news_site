from django.urls import path
from app_apartment.views import AboutView, ApartmentListView, ContactView, NewsFeedView
from app_apartment.feeds import ApartmentNewsFeed
from django.contrib.sitemaps.views import sitemap
from app_apartment.sitemap import NewsSitemap

sitemaps = {
    'rooms': NewsSitemap
}

urlpatterns = [
    path('about/', AboutView.as_view(), name='about'),
    path('apartment_list/', ApartmentListView.as_view(), name='apartment_list'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('<int:pk>', NewsFeedView.as_view(), name='news_feed'),
    path('news_feed/latest/', ApartmentNewsFeed(), name='news_feed_latest'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap')
    ]
