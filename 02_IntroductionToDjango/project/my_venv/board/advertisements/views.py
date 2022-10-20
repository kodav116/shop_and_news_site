from django.shortcuts import render
from django.http import HttpResponse
from advertisements.models import Advertisement


def advertisement_list(request, *args, **kwargs):
    advertisements = Advertisement.objects.all()
    adv1 = advertisements.get(title='Мое первое объявление')
    adv2 = advertisements.get(title='Продам ладу')
    return render(request, 'advertisements/advertisements.html', {
        'advertisements': advertisements, 'adv1': adv1, 'adv2': adv2
    })


def adv_one(request, *args, **kwargs):
    advertisements = Advertisement.objects.all()
    adv1 = advertisements.get(title='Мое первое объявление')
    adv2 = advertisements.get(title='Продам ладу')
    return render(request, 'advertisements/adv_one.html', {
        'advertisements': advertisements, 'adv1': adv1, 'adv2': adv2
    })


def adv_two(request, *args, **kwargs):
    advertisements = Advertisement.objects.all()
    adv1 = advertisements.get(title='Мое первое объявление')
    adv2 = advertisements.get(title='Продам ладу')
    return render(request, 'advertisements/adv_two.html', {
        'advertisements': advertisements, 'adv1': adv1, 'adv2': adv2
    })











