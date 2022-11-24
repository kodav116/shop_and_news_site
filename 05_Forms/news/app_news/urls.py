from django.urls import path
from django.contrib import admin
from app_news.views import NewsFormView, CommentaryFormView, NewsList, UpdateNewsView, \
    login_view, AnotherLoginView, MainView, logout_view, AuthCommentaryForm, register_view, AccountView, \
    UpdateUserView, BlogListView, BlogFormView



urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('admin/', admin.site.urls),
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
    path('blog/blog_list/', BlogListView.as_view()),
    path('blog/<int:pk>/', BlogListView.blogdetail, name='blogdetail'),
    path('blog/new_blog_post/', BlogFormView.as_view(), name='new_blog_post'),
    path('profiles/update_user/', UpdateUserView.as_view(), name='update_user'),

]
