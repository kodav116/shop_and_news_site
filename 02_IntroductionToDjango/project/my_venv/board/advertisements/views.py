from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView


def advertisement_list(request, *args, **kwargs):
    advertisements = [
        'Мастер на час',
        'Мастер на день',
        'Мастер на неделю',
        'Мастер на месяц'
    ]

    return render(request, 'advertisements/advertisement_list.html', {'advertisements': advertisements})


class Advertisements(View):
    def get(self, request):
        advertisements = [
            'Мастер на час',
            'Мастер на день',
            'Мастер на неделю',
            'Мастер на месяц'
        ]
        return render(request, 'advertisements/advertisements.html', {'advertisements': advertisements})

    def post(self, request):
        print(request.POST, 'Запрос на запись успешно выполнен.')
        return render(request, 'advertisements/advertisements.html')


class About(TemplateView):
    template_name = 'advertisements/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Объявления'
        context['description'] = """
        Хотите быстро купить что-то или продать?

        Вывесите объявление здесь!
        """
        return context


class Contacts(TemplateView):
    template_name = 'advertisements/contacts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['address'] = 'г. Краснодар, ул. Очаковская 45'
        context['phone'] = '89999999999'
        context['mail'] = 'django@mail.com'
        return context


class Main(TemplateView):
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = 'О компании'
        context['contacts'] = 'Наши контакты'
        context['advertisements'] = 'Наши объявления'
        context['aboutURL'] = 'advertisements/about/'
        context['contactsURL'] = 'advertisements/contacts/'
        context['advertisementsURL'] = 'advertisements/advertisements/'
        return context

    def post(self, request):
        print(request.POST, 'Запрос на запись успешно выполнен.')
        return render(request, 'main.html')



