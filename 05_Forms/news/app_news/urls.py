from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from app_news.views import NewsFormView, CommentaryFormView, NewsList, UpdateNewsView, \
    login_view, AnotherLoginView, MainView, logout_view, AuthCommentaryForm, register_view, AccountView, \
    UpdateUserView, BlogListView, BlogFormView, update_blog, OffersView
from rest_framework import routers
from app_news.api import AuthorViewSet, BookViewSet, AuthorDetail, BookDetail


urlpatterns = [
    path('i18n', include('django.conf.urls.i18n')),
    path('', MainView.as_view(), name='main'),
    path('profiles/news/', NewsFormView.as_view()),
    path('profiles/comment/', CommentaryFormView.as_view()),
    path('profiles/news_list/', NewsList.as_view()),
    path('profiles/<int:pk>/', NewsList.newsdetail, name='newsdetail'),
    path('profiles/edit/<int:pk>/', UpdateNewsView.as_view(), name='update_news'),
    path('profiles/login/', login_view, name='login'),
    path('profiles/logout/', logout_view, name='logout'),
    path('profiles/another_login/', AnotherLoginView.as_view(), name='another_login'),
    path('users/register/', register_view, name='register'),
    path('users/account/', AccountView.as_view(), name='account'),
    path('users/loyalty_cabinet/', OffersView.as_view(), name='loyalty_cabinet'),
    path('blog/blog_list/', BlogListView.as_view()),
    path('blog/<int:pk>/', BlogListView.blogdetail, name='blogdetail'),
    path('blog/new_blog_post/', BlogFormView.as_view(), name='new_blog_post'),
    path('profiles/update_user/<int:pk>/', UpdateUserView.as_view(), name='update_user'),
    path('blog/upload_blog_posts', update_blog, name='update_blog'),
    path('api/authors/', AuthorViewSet.as_view(), name='author_view'),
    path('api/books/', BookViewSet.as_view(), name='book_view'),
    path('api/authors/<int:pk>/', AuthorDetail.as_view(), name='author_detail'),
    path('api/books/<int:pk/', BookDetail.as_view(), name='book_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)