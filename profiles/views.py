from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib import messages  # import messages
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.forms import AuthenticationForm  # add this
from django.contrib.auth import login, authenticate, logout  # add this
from django.http import HttpResponse
from .models import *

# Create your views here.


def main(request):
    return render(request, 'profiles/main.html')

# def client(request):
#     return HttpResponse('Client')


def spreg(request):
    return render(request, 'profiles/spreg.html')


def serviceproviders(request):
    bookings = Book.objects.all()
    return render(request, 'profiles/sps.html', {'bookings':bookings})


def dashboard(request):
    return render(request, 'profiles/dashboard.html')

def serviceuserdash(request):
    return render(request, 'profiles/serviceuserdash.html')

def signuplogin(request):
    return render(request, 'profiles/jointsinlogin.html')

# def register_request(request):
#     return render(request, 'profiles/signup.html')

# def login(request):
#     return render(request, 'profiles/login.html')


def register_request(request):
	if request.method == "POST":
		form = SignUpForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("profiles:main")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = SignUpForm
	return render (request=request, template_name="profiles/main.html", context={"register_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("profiles:homepage")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="profiles/main.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("profiles:homepage")
