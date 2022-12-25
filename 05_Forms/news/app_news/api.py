from warnings import filters

from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, RetrieveModelMixin, \
    DestroyModelMixin
from rest_framework.generics import GenericAPIView
from app_news.serializers import AuthorSerializer, BookSerializer
from app_news.models import Author, Book
from django_filters.filters import OrderingFilter


class AuthorViewSet(ListModelMixin, CreateModelMixin, GenericAPIView):
    """
    Представление API для получения списка авторов и добавления новых авторов в список.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filterset_fields = ['name']

    def get(self, request):
        return self.list(request)

    def post(self, request, format=None):
        return self.create(request)


class BookViewSet(ListModelMixin, CreateModelMixin, GenericAPIView):
    """
       Представление API для получения списка книг и добавления новых книг в список.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filterset_fields = ['title']
    ordering_fields = ['page_amount']

    def get(self, request):
        return self.list(request)

    def post(self, request, format=None):
        return self.create(request)


class AuthorDetail(UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericAPIView):
    """
    Представление API для получения детальной информации об авторе,
    а также для её редактирования и удаления.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class BookDetail(UpdateModelMixin, RetrieveModelMixin, DestroyModelMixin, GenericAPIView):
    """
    Представление API для получения детальной информации о книге,
    а также для её редактирования и удаления.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
