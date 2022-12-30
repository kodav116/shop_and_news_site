from django import forms
from app_news.models import News, Commentary, BlogPost, BlogImage, Offers
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


class PostFileForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['description', ]

    files = forms.ModelMultipleChoiceField(queryset=BlogImage.objects.all())

    def __init__(self, *args, **kwargs):
        if kwargs.get('instance'):
            initial = kwargs.setdefault('initial', {})
            initial['files'] = [t.pk for t in kwargs['instance'].blogimage_set.all()]

        forms.ModelForm.__init__(self, *args, **kwargs)

    def save(self, commit=True):
        instance = forms.ModelForm.save(self, False)
        old_save_m2m = self.save_m2m

        def save_m2m():
            old_save_m2m()
            instance.blogimage_set.clear()
            instance.blogimage_set.add(*self.cleaned_data['files'])
        self.save_m2m = save_m2m

        if commit:
            instance.save()
            self.save_m2m()

        return instance


class UploadBlogForm(forms.Form):
    file = forms.FileField()


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


class OffersForm(forms.ModelForm):
    class Meta:
        model = Offers
        fields = ['balance']




