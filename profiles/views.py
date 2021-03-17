from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import Serviceprovider
from .models import Booking
from .models import Serviceuser as ServiceuserModel
from .forms import CreateUserForm, ServiceuserForm
from django.contrib import messages  # import messages
# from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.forms import AuthenticationForm  # add this
from django.contrib.auth import authenticate, login, logout  # add this
from .models import *
from .filters import BookingFilter
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import *
# added imports
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes



# Create your views here.

def main(request):
	registerform = CreateUserForm()
	loginform = AuthenticationForm()
	context = {'registerform':registerform, 'loginform':loginform }

	if request.method == 'POST':
		if 'registerbtn' in request.POST:
			registerform = CreateUserForm(request.POST)
			if registerform.is_valid():
				registerform.save()
				user = registerform.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)
				return redirect('profiles:homepage')
			else:
				messages.error(request, "User was not created")
			loginform = AuthenticationForm(data=request.POST)
		elif 'loginbtn' in request.POST:
			loginform = AuthenticationForm(data=request.POST)
			if loginform.is_valid():
				username = loginform.cleaned_data.get('username')
				password = loginform.cleaned_data.get('password')
				user = authenticate(username=username, password=password)
				if user is not None:
					login(request, user)
					# messages.info(request, f"You are now logged in as {username}")
					return redirect('profiles:homepage')
				else:
					messages.error(request, "No user in the system yet")
			else:
				messages.error(request, "Invalid username or password.")
			loginform = AuthenticationForm()
		return render(request = request,
                    template_name = "profiles/main.html")
	return render(request, 'profiles/main.html', context)


def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "profiles/password/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					# messages.success(request, 'A message with reset password instructions has been sent to your inbox.')
					return redirect ("/password_reset/done/")
					# return redirect ("profiles:homepage")

	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="profiles/password/password_reset.html", context={"password_reset_form":password_reset_form})


def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("profiles:homepage")


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

def booking(request):
    return render(request, template_name='profiles/bookingform.html')

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
            return redirect(reverse ('profiles:dashboard'))

    context = {'form': form, serviceusers: serviceusers}
    return render(request,'profiles/serviceuser.html', context)

def updateServiceuser(request, pk):

    serviceusers = ServiceuserModel.objects.get(id=pk)
    form = ServiceuserForm(instance=serviceusers)

    if request.method == 'POST':
        form = ServiceuserForm(request.POST, instance=serviceusers)
        if form.is_valid():
            form.save()
            return redirect(reverse ('profiles:dashboard'))

    context = {'form': form}
    return render(request, 'profiles/serviceuser.html', context) 

def deleteServiceuser(request, pk):
    serviceusers = ServiceuserModel.objects.get(id=pk)
    if request.method == "POST":
        serviceusers.delete()
        return redirect(reverse ('profiles:dashboard'))
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


# def register_request(request):
# 	if request.method == "POST":
# 		form = SignUpForm(request.POST)
# 		if form.is_valid():
# 			user = form.save()
# 			login(request, user)
# 			messages.success(request, "Registration successful." )
# 			return redirect("profiles:main")
# 		messages.error(request, "Unsuccessful registration. Invalid information.")
# 	form = SignUpForm
# 	return render (request=request, template_name="profiles/main.html", context={"register_form":form})

# def login_request(request):
# 	if request.method == "POST":
# 		form = AuthenticationForm(request, data=request.POST)
# 		if form.is_valid():
# 			username = form.cleaned_data.get('username')
# 			password = form.cleaned_data.get('password')
# 			user = authenticate(username=username, password=password)
# 			if user is not None:
# 				login(request, user)
# 				messages.info(request, f"You are now logged in as {username}.")
# 				return redirect("profiles:homepage")
# 			else:
# 				messages.error(request,"Invalid username or password.")
# 		else:
# 			messages.error(request,"Invalid username or password.")
# 	form = AuthenticationForm()
# 	return render(request=request, template_name="profiles/main.html", context={"login_form":form})




# def main(request):
# 	signup_form = CreateUserForm()
# 	login_form = AuthenticationForm()
# 	context = {'signup_form':signup_form, 'login_form':login_form }


# 	if request.method == 'POST':
# 		signup_form = CreateUserForm(request.POST)
# 		if signup_form.is_valid():
# 			signup_form.save()
# 			user = signup_form.cleaned_data.get('username')
# 			messages.success(request, 'Account was created for ' + user)
# 			# return redirect('homepage')
# 		else:
# 			messages.error(request, "User was not created")
	
	
# 		# if request.method == 'POST':
# 		login_form = AuthenticationForm(data=request.POST)
# 		if login_form.is_valid():
# 				# username = request.POST.get('username')
# 				# password = request.POST.get('password')
# 			username = login_form.cleaned_data.get('username')
# 			password = login_form.cleaned_data.get('password')
# 			user = authenticate(username=username, password=password)
# 			if user is not None:
# 				login(request, user)
# 				messages.info(request, f"You are now logged in as {username}")
# 				return redirect('profiles:homepage')
# 			else:
# 				messages.error(request, "Invalid username or password.")
# 		else:
# 			messages.error(request, "Invalid username or password.")
# 		login_form = AuthenticationForm()
# 		return render(request = request,
#                     template_name = "profiles/main.html")
#                     # context={"login_form":login_form})
# 	return render(request, 'profiles/main.html', context)
