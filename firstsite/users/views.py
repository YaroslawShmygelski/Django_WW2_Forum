from django.http import HttpResponse
from django.shortcuts import render


def base(request):
    return HttpResponse('gfdgd')


# Create your views here.
def login_users(request):
    return HttpResponse('login')


def logout_users(request):
    return HttpResponse('logout')
