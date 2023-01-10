from django.urls import path
from app_apartment.views import AboutView, ApartmentListView, ContactView, NewsFeedView

urlpatterns = [
    path('about/', AboutView.as_view(), name='about'),
    path('apartments/apartment_list/', ApartmentListView.as_view(), name='apartment_list'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('apartments/news_feed/', NewsFeedView.as_view(), name='news_feed'),
    ]
