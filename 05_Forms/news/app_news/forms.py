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

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        is_authenticated = kwargs.pop('is_authenticated', False)
        super().__init__(*args, **kwargs)
        if is_authenticated:
            del self.fields['user_name']  # Remove the field itself from the form
            self.instance.user_name = user  # Set the user as the owner


class AuthForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
