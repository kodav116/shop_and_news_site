from warnings import filters

from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.generics import GenericAPIView
from app_news.serializers import AuthorSerializer, BookSerializer
from app_news.models import Author, Book
from django_filters.filters import OrderingFilter


class AuthorViewSet(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filterset_fields = ['name']

    def get(self, request):
        return self.list(request)

    def post(self, request, format=None):
        return self.create(request)


class BookViewSet(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filterset_fields = ['title']
    ordering_fields = ['page_amount']

    def get(self, request):
        return self.list(request)

    def post(self, request, format=None):
        return self.create(request)
