from django.shortcuts import render
from django.views import View
from app_apartment.models import Apartment, RoomType, ApartmentNews


class AboutView(View):

    def get(self, request):
        return render(request, 'about.html')


class ApartmentListView(View):

    def get(self, request):
        return render(request, 'apartment_list.html')


class ContactView(View):

    def get(self, request):
        return render(request, 'contact.html')


class NewsFeedView(View):

    def get(self, request):
        return render(request, 'news_feed.html')





