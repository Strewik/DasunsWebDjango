import os
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Serviceuser as ServiceuserModel
from .forms import *
from django.contrib import messages  # import messages
# from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.forms import AuthenticationForm  # add this
from django.contrib.auth import authenticate, login, logout  # add this
# from .models import *
from .filters import *
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import *
# added imports
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import Group
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.core.paginator import Paginator, EmptyPage


from django.core.mail import send_mail
from django.conf import settings
import smtplib
from email.message import EmailMessage
# import urllib.request
# from django.template.loader import render_to_string

from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only


# Create your views here.

# @unauthenticated_user. This works for separate register and login pages.
# @admin_only
def main(request):
    registerform = CreateUserForm()
    loginform = AuthenticationForm()
    context = {'registerform':registerform, 'loginform':loginform }
    if request.method == 'POST':
        if 'registerbtn' in request.POST:
            registerform = CreateUserForm(request.POST)
            if registerform.is_valid():
                # registerform.save()
                # user = registerform.cleaned_data.get('username')
                user = registerform.save()
                username = registerform.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + username)
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
                    messages.info(request, f"You are now logged in as {username}")
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

# @login_required(login_url='profiles:homepage')
def spreg_save(request):
    
    if request.method != 'POST':
        return render(request, 'profiles:spreg.html')
    else: 
        user = request.user
        fullname = request.POST.get('fullname')
        phone =request.POST.get('phone')
        email = request.POST.get('email')
        nin = request.POST.get('nin')
        dob = request.POST.get('dob')
        gender = request.POST.get('gender')
        phyadd = request.POST.get('phyadd')
        yearexp = request.POST.get('yearexp')
        notmidman = request.POST.get('notmidman')
        skillset = request.POST.get('skillset')
        internet = request.POST.get('internet')
        qualification = request.POST.get('qualification')
        portifolio = request.POST.get('portifolio')
        profession = request.POST.get('profession')
        ref1name = request.POST.get('ref1name')
        ref1title = request.POST.get('ref1title')
        ref1email = request.POST.get('ref1email')
        ref1phone = request.POST.get('ref1phone')
        ref2name = request.POST.get('ref2name')
        ref2title = request.POST.get('ref2title')
        ref2email = request.POST.get('ref2email')
        ref2phone = request.POST.get('ref2phone')
        category = request.POST.get('category')
        service = request.POST.get('service')
        availability = request.POST.get('availability')
        status = request.POST.get('status')
        starttime = request.POST.get('starttime')
        endtime = request.POST.get('endtime')
        pricevisit = request.POST.get('pricevisit')
        terms = request.POST.get('terms')
        
        
        
        ServProv = Serviceprovider(user=user, fullname=fullname, phone=phone, email=email, nin=nin, dob=dob, gender=gender, phyadd=phyadd, yearexp=yearexp, notmidman=notmidman, skillset=skillset, internet=internet, qualification=qualification, portifolio=portifolio, profession=profession, ref1name=ref1name, ref1title=ref1title,ref1email=ref1email, ref1phone=ref1phone, ref2name=ref2name, ref2title=ref2title,ref2email=ref2email, ref2phone=ref2phone, service=service, availability=availability,status=status, starttime=starttime, endtime=endtime, pricevisit=pricevisit, terms=terms,)
        ServProv.save()
        
    return render(request, 'profiles/spregsuccess.html')
    


def spreg(request):
    return render(request, 'profiles/spreg.html',)
          


# @login_required(login_url='profiles:homepage')
# @allowed_users(allowed_roles=['serviceprovider'])
def serviceproviderdash(request):
	bookings = request.user.serviceprovider.booking_set.all()
	context = {'bookings': bookings }
	return render(request, 'profiles/serviceProviderDashboard.html', context)


def spregsuccess(request):
   
    email = EmailMessage(
        'subject',
        'body',
        settings.EMAIL_HOST_USER,
        ['kawooyastevenug@gmail.com'], 
        )
    email.fail_silently=False
    email.send()
      
    return render(request, 'profiles/spregsuccess.html')

# @login_required(login_url='profiles:homepage')
# @allowed_users(allowed_roles=['admin'])
def dashboard(request):
    bookings = Booking.objects.all()
    serviceproviders = Serviceprovider.objects.all()
    serviceusers = ServiceuserModel.objects.all()
    total_serviceproviders = serviceproviders.count()
    pendingcount_serviceproviders = serviceproviders.filter(status='Pending').count()
    pending_serviceproviders = serviceproviders.filter(status='Pending')
    active_serviceproviders = serviceproviders.filter(status='Active')
    activecount_serviceproviders = serviceproviders.filter(status='Active').count()
    suspended_serviceproviders = serviceproviders.filter(status='Suspended')
    suspendedcount_serviceproviders = serviceproviders.filter(status='Suspended').count()
    
    total_serviceusers = serviceusers.count()
    total_bookings = bookings.count()
    
    myFilter = ServiceproviderFilter(request.GET, queryset=active_serviceproviders)
    active_serviceproviders = myFilter.qs
    
    paginator = Paginator(serviceusers, 5)
    page_number = request.GET.get('page', 1)
    
    try:
        page_obj = paginator.get_page(page_number)
    except EmptyPage:
        page_number(1)

    context = {'bookings': bookings, 'serviceproviders': serviceproviders, 'serviceusers': serviceusers,
               'total_serviceproviders': total_serviceproviders, 'pending_serviceproviders': pending_serviceproviders,
               'active_serviceproviders': active_serviceproviders, 'activecount_serviceproviders': activecount_serviceproviders, 'suspended_serviceproviders': suspended_serviceproviders,
               'pendingcount_serviceproviders': pendingcount_serviceproviders, 'suspendedcount_serviceproviders': suspendedcount_serviceproviders,
               'total_serviceusers': total_serviceusers, 
               'total_bookings':total_bookings, 'myFilter': myFilter,
               'page_obj': page_obj}
    return render(request, 'profiles/dashboard.html', context)


# @login_required(login_url='profiles:homepage')
# @allowed_users(allowed_roles=['serviceuser', 'admin'])
def createBooking(request, pk):
	# serviceusers = ServiceuserModel.objects.all()
	# serviceuser = ServiceuserModel.objects.get(id=pk)
	serviceuser = request.user.serviceuser
	serviceprovider = Serviceprovider.objects.get(id=pk)
	bookingform = BookingForm()
	
	if request.method == 'POST':
		bookingform = BookingForm(request.POST)

		if bookingform.is_valid():
			serviceuser = bookingform.cleaned_data.get('serviceuser')
			serviceprovider = bookingform.cleaned_data.get('serviceprovider')
			# mybookingform = bookingform.save()
			# print('Printing mybookingform:', mybookingform.serviceprovider)
			bookingform.save()
			return redirect(reverse ('profiles:serviceuserdash'))

	context = {'bookingform': bookingform, 'serviceprovider':serviceprovider, 'serviceuser':serviceuser}
	return render(request,'profiles/bookingform.html', context)

 

# @login_required(login_url='profiles:homepage')
# @allowed_users(allowed_roles=['serviceprovider', 'admin'])
def updateBookingStatus(request, pk):
	serviceusers = ServiceuserModel.objects.all()
	serviceprovider = Serviceprovider.objects.get(id=pk)
	# booking = Booking.objects.get(id=pk)

	if request.method == 'POST':
		print('Printing post:', request.POST)
		
		# First, you should retrieve the team instance you want to update
		booking = Booking.objects.get(id=request.POST['id'])

		# Next, you update the status
		if request.POST.get('status'):
			booking.status = request.POST.get('status')
			booking.save()
			return redirect(reverse ('profiles:serviceproviderdash'))

	context = {'serviceusers':serviceusers, 'booking':booking, 'serviceprovider':serviceprovider}
	return render(request,'profiles/serviceProviderDashboard.html', context)


# @login_required(login_url='profiles:homepage')
# @allowed_users(allowed_roles=['serviceuser'])
def serviceuserdash(request):
	bookings = request.user.serviceuser.booking_set.all()
	# bookings = mybookings.order_by('-date_created')
	# print('my bookings:', bookings)
	# for booking in bookings:
	# 	booking.service_hours = (int(float(booking.endtime)) - int(float(booking.starttime)))
	# total_bookings = bookings.count()
	# ongoing = bookings.filter(status='Ongoing').count()
	# completed = bookings.filter(status='Completed').count()
	# cancelled = bookings.filter(status='Cancelled').count()

	# context = {'bookings': bookings, 'total_bookings': total_bookings, 'ongoing': ongoing, 'completed': completed, 'cancelled': cancelled,}
	context = {'bookings': bookings}

	return render(request, 'profiles/serviceuserdash.html', context)


# @login_required(login_url='profiles:homepage')
# @allowed_users(allowed_roles=['serviceuser'])
def serviceUserProfile(request):
    serviceuser = request.user.serviceuser
    username = request.user
    firstname = serviceuser.firstname
    lastname = serviceuser.lastname
    phone = serviceuser.phone
    email = serviceuser.email
    date = serviceuser.date_created
    profile_pic = serviceuser.profile_pic
    context = {'username':username, 'firstname':firstname, 'lastname':lastname, 'phone':phone, 'email':email, 'date':date, }
    return render(request, 'profiles/serviceuserProfile.html', context)



# @login_required(login_url='profiles:homepage')
# @allowed_users(allowed_roles=['serviceuser', 'admin'])
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

# @login_required(login_url='profiles:homepage')
# @allowed_users(allowed_roles=['admin'])
def updateServiceprovider(request, pk):
    
    serviceprovider = Serviceprovider.objects.get(id=pk)
    form = ServiceproviderForm(instance=serviceprovider)

    if request.method == 'POST':
        form = ServiceproviderForm(request.POST, instance=serviceprovider)
        if form.is_valid():
            form.save()
            return redirect(reverse ('profiles:dashboard'))

    context = {'form': form}
    return render(request, 'profiles/serviceprovider.html', context) 



# @login_required(login_url='profiles:homepage')
# @allowed_users(allowed_roles=['admin'])
def deleteServiceuser(request, pk):
    serviceusers = ServiceuserModel.objects.get(id=pk)
    if request.method == "POST":
        serviceusers.delete()
        return redirect(reverse ('profiles:dashboard'))
    context = {'item': serviceusers}
    return render(request, 'profiles/deleteServiceuser.html', context) 

# @login_required(login_url='profiles:homepage')
# @allowed_users(allowed_roles=['admin'])
def deleteServiceprovider(request, pk):
    serviceprovider = Serviceprovider.objects.get(id=pk)
    if request.method == "POST":
        serviceprovider.delete()
        return redirect(reverse ('profiles:dashboard'))
    context = {'item': serviceprovider}
    return render(request, 'profiles/deleteServiceprovider.html', context) 

@login_required(login_url='profiles:homepage')
@allowed_users(allowed_roles=['serviceuser'])
def serviceProviderProfile(request):
    serviceprovider = request.user.serviceprovider
    username = request.user
    fullname = serviceprovider.fullname
    gender = serviceprovider.gender
    phone = serviceprovider.phone
    email = serviceprovider.email
    address = serviceprovider.phyadd
    service = serviceprovider.service
    context = {'username':username, 'fullname':fullname, 'gender':gender, 'phone':phone, 'email':email, 'address':address, 'service':service}
    return render(request, 'profiles/serviceproviderProfile.html', context)


@login_required(login_url='profiles:homepage')
@allowed_users(allowed_roles=['serviceuser', 'admin'])
def captioningList(request):
	serviceproviders = Serviceprovider.objects.all()
	context = {'serviceproviders': serviceproviders}
	return render(request, 'profiles/splist/captioning.html', context)


@login_required(login_url='profiles:homepage')
@allowed_users(allowed_roles=['serviceuser', 'admin'])
def internationalInterpList(request):
	serviceproviders = Serviceprovider.objects.all()
	context = {'serviceproviders': serviceproviders}
	return render(request, 'profiles/splist/internationalInterp.html', context)


@login_required(login_url='profiles:homepage')
@allowed_users(allowed_roles=['serviceuser', 'admin'])
def mobGuideList(request):
	serviceproviders = Serviceprovider.objects.all()
	context = {'serviceproviders': serviceproviders}
	return render(request, 'profiles/splist/mobGuide.html', context)


@login_required(login_url='profiles:homepage')
@allowed_users(allowed_roles=['serviceuser', 'admin'])
def personalSupportList(request):
	serviceproviders = Serviceprovider.objects.all()
	context = {'serviceproviders': serviceproviders}
	return render(request, 'profiles/splist/personalSupport.html', context)


@login_required(login_url='profiles:homepage')
@allowed_users(allowed_roles=['serviceuser', 'admin'])
def ugandanInterpList(request):
	serviceproviders = Serviceprovider.objects.all()
	context = {'serviceproviders': serviceproviders}
	return render(request, 'profiles/splist/ugandaInterpreter.html', context)


@login_required(login_url='profiles:homepage')
@admin_only
def generalDash(request):
	return render(request, 'profiles/generalDashboard.html')


# @login_required(login_url='profiles:homepage')
# @allowed_users(allowed_roles=['serviceuser', 'admin'])
def spList(request):
    serviceproviders = Serviceprovider.objects.all()
    context = {'serviceproviders': serviceproviders}
    return render(request, 'profiles/splist/allServiceProviders.html', context)
