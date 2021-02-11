from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'profiles/home.html')

def client(request):
    return HttpResponse('Client')

def serviceprovider(request):
    return render(request, 'profiles/serviceprovider.html')

def dashboard(request):
    return render(request, 'profiles/dashboard.html')
