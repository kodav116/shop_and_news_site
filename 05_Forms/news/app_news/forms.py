from django import forms
from app_news.models import News, Commentary



class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        ordering = ('created_at')
        fields = ['title', 'description', 'is_active']


class CommentaryForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ['user_name', 'news_at', 'comment']


class AuthCommentaryForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = ['news_at', 'comment']


class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

