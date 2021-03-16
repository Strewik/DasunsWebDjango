from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import Serviceprovider
from .models import Booking
from .models import Serviceuser as ServiceuserModel

from .forms import ServiceuserForm


# Create your views here.

def main(request):
    return render(request, 'profiles/main.html')

def client(request):
    return HttpResponse('Client')


def spreg(request):
    return render(request, 'profiles/spreg.html')


def sps(request):
    bookings = Booking.objects.all()

    context = {'bookings':bookings}
    return render(request, 'profiles/sps.html',context )


def serviceprovider(request):
    serviceproviders = ServiceProvider.objects.all()

    context = {'serviceproviders':serviceproviders}
    return render(request, 'profiles/sps.html', context)


def dashboard(request):
    bookings = Booking.objects.all()
    serviceproviders = Serviceprovider.objects.all()
    serviceusers = ServiceuserModel.objects.all()

    context = {'bookings': bookings, 'serviceproviders': serviceproviders, 'serviceusers': serviceusers}
    return render(request, 'profiles/dashboard.html', context)

def serviceuserdash(request):
    return render(request, 'profiles/serviceuserdash.html')

def signuplogin(request):
    return render(request, 'profiles/jointsinlogin.html')

def serviceuser(request):

    serviceusers = ServiceuserModel.objects.all()

    form = ServiceuserForm()
    if request.method == 'POST':
        # print('Printing post:', request.POST)
        form = ServiceuserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse ('dashboard'))

    context = {'form': form, serviceusers: serviceusers}
    return render(request,'profiles/serviceuser.html', context)

def updateServiceuser(request, pk):

    serviceusers = ServiceuserModel.objects.get(id=pk)
    form = ServiceuserForm(instance=serviceusers)

    if request.method == 'POST':
        form = ServiceuserForm(request.POST, instance=serviceusers)
        if form.is_valid():
            form.save()
            return redirect(reverse ('dashboard'))

    context = {'form': form}
    return render(request, 'profiles/serviceuser.html', context) 

def deleteServiceuser(request, pk):
    serviceusers = ServiceuserModel.objects.get(id=pk)
    if request.method == "POST":
        serviceusers.delete()
        return redirect(reverse ('dashboard'))
    context = {'item': serviceusers}
    return render(request, 'profiles/deleteServiceuser.html', context) 

 

# def spreg(request):
#     return render(request, 'profiles/spreg.html')
# def dashboard(request):
#     # book = Book.objects.all()
#     return render(request, 'profiles/dashboard.html',{'bookings':bookings})

# def serviceproviders(request):
#     bookings = Book.objects.all()
#     return render(request, 'profiles/sps.html', {'bookings':bookings})


# def dashboard(request):
#     return render(request, 'profiles/dashboard.html')
# def dashboard(request):
#     return render(request, 'profiles/dashboard.html')
