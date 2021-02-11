from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('Home')

def client(request):
    return HttpResponse('Client')

def serviceprovider(request):
    return HttpResponse('Service Provider')

def dasuns(request):
    return HttpResponse('Administration Dashboard')
