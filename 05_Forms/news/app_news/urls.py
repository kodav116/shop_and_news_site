import patterns as patterns
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from django.conf import settings
from app_news.views import NewsFormView, CommentaryFormView, NewsList, UpdateNewsView, \
    login_view, AnotherLoginView, MainView, logout_view, AuthCommentaryForm, register_view, AccountView, \
    UpdateUserView, BlogListView, BlogFormView, update_blog, UserCabinetView, update_balance, ShopListView
from rest_framework import routers
from app_news.api import AuthorViewSet, BookViewSet, AuthorDetail, BookDetail
from . import views
import debug_toolbar


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
    path('users/user_cabinet/', UserCabinetView.as_view(), name='user_cabinet'),
    path('users/update_balance/', update_balance, name='update_balance'),
    path('users/shop_list/', ShopListView.as_view(), name='shop_list'),
    path('blog/blog_list/', BlogListView.as_view()),
    path('blog/<int:pk>/', BlogListView.blogdetail, name='blogdetail'),
    path('blog/new_blog_post/', BlogFormView.as_view(), name='new_blog_post'),
    path('profiles/update_user/<int:pk>/', UpdateUserView.as_view(), name='update_user'),
    path('blog/upload_blog_posts', update_blog, name='update_blog'),
    path('api/authors/', AuthorViewSet.as_view(), name='author_view'),
    path('api/books/', BookViewSet.as_view(), name='book_view'),
    path('api/authors/<int:pk>/', AuthorDetail.as_view(), name='author_detail'),
    path('api/books/<int:pk/', BookDetail.as_view(), name='book_detail'),
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/', views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/', views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail, name='cart_detail'),
    path('__debug__/', include(debug_toolbar.urls)),
    path('apartments/', include('app_apartment.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
