from django.urls import path
from .import views


urlpatterns = [
    path('', views.advertisement_list, name='advertisement_list'),
    path('first_course', views.first_course, name='first_course'),
    path('second_course', views.second_course, name='second_course'),
    path('third_course', views.third_course, name='third_course'),
    path('fourth_course', views.fourth_course, name='fourth_course'),
    path('fifth_course', views.fifth_course, name='fifth_course')
]