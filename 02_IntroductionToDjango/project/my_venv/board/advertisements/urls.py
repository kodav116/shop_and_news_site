from django.urls import path
from . import views


urlpatterns = [
    path('', views.advertisement_list, name='advertisement_list'),
    path('adv_one', views.adv_one, name='adv_one'),
    path('adv_two', views.adv_two, name='adv_two')
]