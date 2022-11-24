from django import forms
from app_news.models import News, Commentary, BlogPost
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        ordering = ['created_at']
        fields = ['title', 'description']


class CommentaryForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ['user_name', 'news_at', 'comment']


class AuthCommentaryForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ['news_at', 'comment']


class BlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['description']


class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class ExtendedRegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Имя')
    last_name = forms.CharField(max_length=30, required=False, help_text='Фамилия')
    email = forms.EmailField()
    date_of_birth = forms.DateField(required=True, help_text='Дата рождения')
    city = forms.CharField(max_length=36, required=False, help_text='Город')

    class Meta:
        model = User
        fields = {'username', 'first_name', 'last_name', 'email', 'password1', 'password2',}



