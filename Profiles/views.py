from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def main(request):
    return render(request, 'profiles/main.html')

def client(request):
    return HttpResponse('Client')

def serviceprovider(request):
    return render(request, 'profiles/serviceprovider.html')

def dashboard(request):
    return render(request, 'profiles/dashboard.html')
