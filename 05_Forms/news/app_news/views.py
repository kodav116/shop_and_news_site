from django.shortcuts import render
from app_news.forms import NewsForm, CommentaryForm
from app_news.models import News, Commentary
from django.views import View
from django.views.generic import ListView


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


class NewsList(ListView):

    def get(self, request):
        return render(request, 'profiles/news_list.html', context={
            'news_list': News.objects.filter(is_active=True).order_by('-created_at')}
                      )

    def newsdetail(request, pk):
        news_report = News.objects.get(id=pk)
        comment_form = CommentaryForm()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.news_report = news_report(id=pk)
            new_comment.save()
        return render(request, 'profiles/news_report.html', {'news_report': news_report,
                                                             'comment_form': comment_form
                                                             })

    def news_comments(self, request, pk):
        post = News.objects.get( News, status='published'
                                 )

        comments = post.comments.filter(active=True)

        new_comment = None

        if request.method == 'POST':
            comment_form = CommentaryForm(data=request.POST)
            if comment_form.is_valid():
                new_comment = comment_form.save(commit=False)
                new_comment.post = post(id=pk)
                new_comment.save()
        else:
            comment_form = CommentaryForm()
        return render(request,
                      'profiles/comment.html/',
                      {'post': post,
                       'comments': comments,
                       'new_comment': new_comment,
                       'comment_form': comment_form,
                       })