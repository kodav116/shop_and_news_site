from django.shortcuts import render
from django.http import HttpResponse


def advertisement_list(request, *args, **kwargs):
    return render(request, 'advertisements/advertisement_list.html', {})


def first_course(request, *args, **kwargs):
    return render(request, 'advertisements/first_course.html', {})


def second_course(request, *args, **kwargs):
    return render(request, 'advertisements/second_course.html', {})


def third_course(request, *args, **kwargs):
    return render(request, 'advertisements/third_course.html', {})


def fourth_course(request, *args, **kwargs):
    return render(request, 'advertisements/fourth_course.html', {})


def fifth_course(request, *args, **kwargs):
    return render(request, 'advertisements/fifth_course.html', {})

