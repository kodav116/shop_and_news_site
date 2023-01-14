from django.shortcuts import render
from django.views import View, generic
from app_apartment.models import Apartment, RoomType, ApartmentNews


class AboutView(View):

    def get(self, request):
        return render(request, 'about.html')


class ApartmentListView(generic.ListView):
    model = RoomType
    template_name = 'apartment_list.html'


class ContactView(View):

    def get(self, request):
        return render(request, 'contact.html')


class NewsFeedView(generic.DetailView):
    model = ApartmentNews
    template_name = 'news_feed.html'





