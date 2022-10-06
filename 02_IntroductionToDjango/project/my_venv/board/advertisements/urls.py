from django.urls import path
from . import views


urlpatterns = [
    path('', views.advertisement_list, name='advertisement_list'),
    path('main/advertisements/', views.Advertisements.as_view()),
    path('main/about/', views.About.as_view()),
    path('main/contacts/', views.Contacts.as_view()),
    path('main/', views.Main.as_view())
    ]