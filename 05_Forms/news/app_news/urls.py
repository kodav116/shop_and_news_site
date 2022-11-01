from django.urls import path, include
from django.contrib import admin
from app_news.views import NewsFormView, CommentaryFormView
from app_news.views import NewsList

from . import views

urlpatterns = [
    path('profiles/news/', NewsFormView.as_view()),
    path('profiles/comment/', CommentaryFormView.as_view()),
    path('profiles/news_list/', NewsList.as_view()),
    path('profiles/<int:pk>/', NewsList.newsdetail, name='newsdetail'),
    path('profiles/<int:pk>/', NewsList.news_comments, name='news_comments')
]
