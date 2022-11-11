from django.urls import path
from django.contrib import admin
from app_news.views import NewsFormView, CommentaryFormView, NewsList, UpdateNewsView, login_view, AnotherLoginView, MainView



urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('admin/', admin.site.urls),
    path('profiles/news/', NewsFormView.as_view()),
    path('profiles/comment/', CommentaryFormView.as_view()),
    path('profiles/news_list/', NewsList.as_view()),
    path('profiles/<int:pk>/', NewsList.newsdetail, name='newsdetail'),
    path('profiles/edit/<int:pk>/', UpdateNewsView.as_view(), name='update_news'),
    path('profiles/login/', login_view, name='login'),
    path('profiles/another_login/', AnotherLoginView.as_view(), name='another_login')
]
