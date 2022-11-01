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
