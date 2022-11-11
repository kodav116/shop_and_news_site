from django import forms
from app_news.models import News, Commentary


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        ordering = ('created_at')
        fields = '__all__'


class CommentaryForm(forms.ModelForm):
    class Meta:
        model = Commentary
        fields = '__all__'


class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
