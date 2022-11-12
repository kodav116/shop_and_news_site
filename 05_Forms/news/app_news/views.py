from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render
from app_news.forms import NewsForm, CommentaryForm, AuthForm
from app_news.models import News, Commentary
from django.views import View
from django.views.generic import UpdateView
from django.contrib.auth.views import LoginView


class MainView(View):
    def get(self, request):
        return render(request, 'profiles/main.html')


class NewsFormView(View):

    def get(self, request):
        news_form = NewsForm()
        return render(request, 'profiles/news.html', context={'news_form': news_form})

    def post(self, request):
        news_form = NewsForm(request.POST)
        if news_form.is_valid():
            news_form.save()
        return render(request, 'profiles/news.html', context={'news_form': news_form})


class CommentaryFormView(View):

    def get(self, request):
        comment_form = CommentaryForm()
        return render(request, 'profiles/comment.html', context={'comment_form': comment_form})

    def post(self, request):
        comment_form = CommentaryForm(request.POST)
        if comment_form.is_valid():
            comment_form.save()
        return render(request, 'profiles/comment.html', context={'comment_form': comment_form})


class NewsList(View):

    def get(self, request):
        return render(request, 'profiles/news_list.html', context={
            'news_list': News.objects.filter(is_active=True).order_by('-created_at')}
                      )

    def newsdetail(request, pk):
        news_report = News.objects.get(id=pk)
        comment_form = CommentaryForm(request.POST or None, prefix='comment',
                                      is_authenticated=request.user.is_authenticated)
        form = comment_form
        if form.is_valid():
            comment = form.save(commit=False)
            comment.news_report = news_report
            comment.save()
        return render(request, 'profiles/news_report.html', {'news_report': news_report,
                                                             'comment_form': comment_form,
                                                             'comments': Commentary.objects.filter(news_at_id=pk)})


    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs



class UpdateNewsView(UpdateView):
    model = News
    template_name = 'profiles/update_news.html/'
    fields = '__all__'


def login_view(request):
    if request.method == 'POST':
        auth_form = AuthForm(request.POST)
        if auth_form.is_valid():
            username = auth_form.cleaned_data['username']
            password = auth_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Вы успешно вошли в систему.')
                else:
                    auth_form.add_error('__all__', 'Ошибка! Учетная запись не активна.')
            else:
                auth_form.add_error('__all__', 'Ошибка! Проверьте правильность написания логина и пароля.')

    else:
        auth_form = AuthForm()
        context = {
            'form': auth_form
        }
        return render(request, 'profiles/login.html', context=context)


class AnotherLoginView(LoginView):
    template_name = 'profiles/login.html'


def logout_view(request):
    logout(request)
    return HttpResponse('Вы успешно вышли из своего аккаунта.')
