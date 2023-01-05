from _csv import reader

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from app_news.forms import NewsForm, CommentaryForm, AuthForm, AuthCommentaryForm, ExtendedRegisterForm, \
    PostFileForm, UploadBlogForm, OffersForm
from app_news.models import News, Commentary, Profile, BlogPost, Offers, Product, Shops
from django.views import View
from django.views.generic import UpdateView
from django.contrib.auth.views import LoginView
from cart.cart import Cart
import logging

logger = logging.getLogger(__name__)


class MainView(View):

    def get(self, request):
        return render(request, 'profiles/main.html')


class BlogFormView(View):

    def get(self, request):
        blog_form = PostFileForm()
        return render(request, 'blog/new_blog_post.html', context={'blog_form': blog_form})

    def post(self, request):
        if request.method == 'POST':
            if request.user.has_perm('app_news.can_publish'):
                blog_form = PostFileForm(request.POST, request.FILES)
                if blog_form.is_valid():
                    files = request.FILES.getlist('file_field')
                    for f in files:
                        instance = BlogPost(file=f)
                        instance.user = request.user
                        instance.save()
                    order = blog_form.save(commit=False)
                    order.user = request.user
                    order.save()
                    return redirect('/')
            else:
                raise PermissionDenied
        else:
            blog_form = PostFileForm()
        return render(request, 'blog/new_blog_post.html', context={'blog_form': blog_form})


class BlogListView(View):

    def get(self, request):
        return render(request, 'blog/blog_list.html', context={
            'blog_list': BlogPost.objects.filter(is_active=True)}
                      )

    def blogdetail(request, pk):
        blog_post = BlogPost.objects.get(id=pk)
        return render(request, 'blog/blog_detail.html', {'blog_post': blog_post})


def update_blog(request):
    if request.method == 'POST':
        upload_blog_form = UploadBlogForm(request.POST, request.FILES)
        if upload_blog_form.is_valid():
            blog_file = upload_blog_form.cleaned_data['file'].read()
            blog_str = blog_file.decode('latin-1').split('\n')
            csv_reader = reader(blog_str, delimiter=';', quotechar='"')
            for row in csv_reader:
                BlogPost.objects.filter(created_at=row[0]).update(description=row[1])
            return HttpResponse(content='Посты добавлены', status=200)
    else:
        upload_blog_form = UploadBlogForm()

    context = {
        'form': upload_blog_form
    }
    return render(request, 'blog/upload_blog_posts.html', context=context)


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
    fields = ['title', 'description']


class UpdateUserView(UpdateView):
    model = User
    template_name = 'profiles/update_profile.html/'
    fields = ['username', 'first_name', 'last_name']
    success_url = '/'


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
                    logger.info(f'Пользователь {request.user} аутентифицирован успешно.')
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


class UserCabinetView(View):

    def get(self, request):
        if request.user.is_authenticated:
            logger.info('Пользователь аутентифицирован. Открываем кабинет пользователя.')
            context = {'cabinet': Offers.objects.get(user=request.user)}
            return render(request, 'users/user_cabinet.html', context=context)
        else:
            raise PermissionDenied


class ShopListView(View):

    def get(self, request):
        if request.user.is_authenticated:
            logger.info('Пользователь аутентифицирован. Открываем список товаров.')
            context = {'wares': Product.objects.select_related('shop').all()}
            return render(request, 'users/shop_list.html', context=context)
        else:
            raise PermissionDenied


def update_balance(request):
    offer = Offers.objects.get(user=request.user)
    offers_id = offer.id
    offer1 = get_object_or_404(Offers, id=offers_id)
    form = OffersForm(request.POST or None, instance=offer1)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.balance += Offers.objects.get(user=request.user).balance
        instance.save()
        logger.info('Баланс пополнен успешно.')
        return redirect('user_cabinet')
    return render(request, 'users/update_balance.html', {'form': form})


@login_required
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("shop_list")


@login_required
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required
def item_decrement(request, id):
    cabinet = Offers.objects.get(user=request.user)
    cart = Cart(request)
    product = Product.objects.get(id=id)
    if product:
        cabinet.balance -= product.price
        logger.info(f'С баланса списано {product.price} баллов.')
        cabinet.purchase_history += product.price
        product.sales += 1
        product.quantity -= 1
        if cabinet.purchase_history >= 10000:
            cabinet.status = 1
            logger.info(f'Cтатус {cabinet.user} теперь равен {cabinet.status}')
        if cabinet.purchase_history >= 100000:
            cabinet.status = 2
            logger.info(f'Cтатус {cabinet.user} теперь равен {cabinet.status}')
        cabinet.save()
        product.save()
        logger.info('Товар куплен успешно.')
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required
def cart_clear(request):
    cabinet = Offers.objects.get(user=request.user)
    cart1 = Cart(request)
    cart1.clear()
    return redirect("cart_detail")


@login_required
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')


