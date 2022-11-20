from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import permission_required
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import render, redirect
from app_news.forms import NewsForm, CommentaryForm, AuthForm, AuthCommentaryForm, ExtendedRegisterForm
from app_news.models import News, Commentary, Profile
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
        if request.user.has_perm('app_news.can_publish'):
            news_form = NewsForm(request.POST)
            if news_form.is_valid():
                news_form.save()
            return render(request, 'profiles/news.html', context={'news_form': news_form})
        else:
            raise PermissionDenied



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
        if request.user.is_authenticated:
            comment_form = AuthCommentaryForm(request.POST)
            form = comment_form
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user_name = request.user.username
                comment.news_report = news_report
                comment.save()
        else:
            comment_form = CommentaryForm(request.POST)
            form = comment_form
            if form.is_valid():
                form.cleaned_data['user_name'] = 'Anonymous'
                comment = form.save(commit=False)
                comment.user_name = comment.user_name + ' -Anonymous'
                comment.news_report = news_report
                comment.save()
        return render(request, 'profiles/news_report.html', {'news_report': news_report,
                                                             'comment_form': comment_form,
                                                             'comments': Commentary.objects.filter(news_at_id=pk)})


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


def register_view(request):
    if request.method == "POST":
        form = ExtendedRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            date_of_birth = form.cleaned_data.get('date_of_birth')
            city = form.cleaned_data.get('city')
            Profile.objects.create(
                user=user,
                city=city,
                date_of_birth=date_of_birth
            )
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = ExtendedRegisterForm()
    return render(request, 'users/register.html', {'form': form})


class AccountView(View):
    def get(self, request):
        return render(request, 'users/account.html')
