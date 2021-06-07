import os
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Serviceuser as ServiceuserModel
from .forms import *
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm  
from django.contrib.auth import authenticate, login, logout  
from .filters import *
from django.contrib.auth.forms import *
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
# from email.message import EmailMessage
from django.core.mail import EmailMessage
# import urllib.request
from django.template.loader import render_to_string

from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.core.files.storage import FileSystemStorage
from datetime import date, time, datetime
# from django.utils import timezone


# Create your views here.

def main(request):
    registerform = CreateUserForm()
    loginform = AuthenticationForm()
    context = {'registerform':registerform, 'loginform':loginform }
    if request.method == 'POST':
        if 'registerbtn' in request.POST:
            registerform = CreateUserForm(request.POST or None)
            if registerform.is_valid():
                user = registerform.save()
                username = registerform.cleaned_data.get('username')
                password = registerform.cleaned_data.get('password1')
                user = authenticate(username=username, password=password)
                login(request, user)
                messages.success(request, 'Account was created for ' + username +' and logged in')
                return redirect('profiles:homepage')
            else:
                username = registerform.data['username']
                email = registerform.data['email']
                password1 = registerform.data['password1']
                password2 = registerform.data['password2']
                for msg in registerform.errors.as_data():
                    if msg == 'username' and User.objects.filter(username=username).exists():
                        messages.error(request, f"username '{username}' already exists, choose another one")
                    if msg == 'email' and User.objects.filter(email=email).exists():
                        messages.error(request, f"This Email address '{email}' is already in use. Please provide a different email address.")
                    elif msg == 'email':
                        messages.error(request, f"Declared email '{email}' is not valid")
                    if msg == 'password2' and password1 == password2:
                        messages.error(request, f"Selected password: '{password1}' is not strong enough,it should have atleast 8 aphanumeric characters and not similar to your username")
                    elif msg == 'password2' and password1 != password2:
                        messages.error(request, f"Password: '{password1}' and Confirmation Password: '{password2}' do not match")
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
        qualification = request.FILES['qualification']
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
        service = request.POST.getlist('service')
        availability = request.POST.getlist('availability')
        status = request.POST.get('status')
        starttime = request.POST.get('starttime')
        endtime = request.POST.get('endtime')
        pricevisit = request.POST.get('pricevisit')
        terms = request.POST.get('terms')
        print('Printing services', service)
        print('Printing availability', availability)
        print('Printing services array', service[2])
        
        
        ServProv = Serviceprovider(user=user, fullname=fullname, phone=phone, email=email, nin=nin, dob=dob, gender=gender, 
                                   phyadd=phyadd, yearexp=yearexp, notmidman=notmidman, skillset=skillset, internet=internet, 
                                   qualification=qualification, portifolio=portifolio, profession=profession, ref1name=ref1name, 
                                   ref1title=ref1title,ref1email=ref1email, ref1phone=ref1phone, ref2name=ref2name, ref2title=ref2title,
                                   ref2email=ref2email, ref2phone=ref2phone, service=service, availability=availability,status=status, 
                                   starttime=starttime, endtime=endtime, pricevisit=pricevisit, terms=terms,)
        ServProv.save()
        
        print('Printing them', Serviceprovider.service)
    return render(request, 'profiles/spregsuccess.html')


def spreg(request):

    return render(request, 'profiles/spreg.html',)

@login_required(login_url='profiles:homepage')
def rating(request):
    return render(request, 'profiles/rating.html',)


@login_required(login_url='profiles:homepage')
def rating_save(request):
    # if request.method == 'POST':
    #     count = Rating(request.POST)
    #     print(count)
    # return render(request, 'profiles/rating.html',)
    
    if request.method != 'POST':
        return render(request, 'profiles:rating.html')
    else: 
        star = request.POST.get("star")
        comment = request.POST.get('comment')
        
    Rate = Rating(star=star, comment=comment,)
    Rate.save()

          

@login_required(login_url='profiles:homepage')
@allowed_users(allowed_roles=['serviceprovider'])
def serviceproviderdash(request):
    bookings = request.user.serviceprovider.booking_set.all()

    today_date = datetime.now().date()
    time_now = datetime.now().time()
    context = {'bookings': bookings, 'time_now':time_now, 'today_date':today_date }
    print('Printing today_date', today_date)
    print('Printing time_now', time_now)

    return render(request, 'profiles/serviceProviderDashboard.html', context)


def spregsuccess(request):
          
    return render(request, 'profiles/spregsuccess.html')

@login_required(login_url='profiles:homepage')
@allowed_users(allowed_roles=['admin'])
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
    
    userFilter = ServiceproviderFilter(request.GET, queryset=serviceusers)
    serviceusers = userFilter.qs
    
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


@login_required(login_url='profiles:homepage')
@allowed_users(allowed_roles=['serviceuser', 'admin'])
def createBooking(request, pk):
    serviceuser = request.user.serviceuser
    serviceprovider = Serviceprovider.objects.get(id=pk)
    bookingform = BookingForm()

    if request.method == 'POST':
        bookingform = BookingForm(request.POST)

        if bookingform.is_valid():
            serviceuser = bookingform.cleaned_data.get('serviceuser')
            serviceprovider = bookingform.cleaned_data.get('serviceprovider')
            bookingform.save()
            return redirect(reverse ('profiles:bookingsuccess', kwargs={"pk": serviceprovider.id}))


    context = {'bookingform': bookingform, 'serviceprovider':serviceprovider, 'serviceuser':serviceuser}
    return render(request,'profiles/bookingform.html', context)


def bookingdetails(request, pk):
    booking = Booking.objects.get(id=pk)
    name = booking.name
    phone = booking.phone
    email = booking.email
    meetplace = booking.meetplace
    meetdate = booking.meetdate
    starttime = booking.starttime
    endtime = booking.endtime
    serviceuser = booking.serviceuser
    serviceprovider = booking.serviceprovider
    date = booking.date_created
    status = booking.status
    context = {'name':name, 'phone':phone,  'email':email, 'meetplace':meetplace, 'meetdate':meetdate, 'starttime':starttime, 'endtime':endtime, 'serviceuser':serviceuser, 'serviceprovider':serviceprovider, 'date':date, 'status':status}
    return render(request, 'profiles/bookingdetails.html', context)


@login_required(login_url='profiles:homepage')
@allowed_users(allowed_roles=['serviceuser'])
def bookingsuccess(request, pk):
    serviceprovider = Serviceprovider.objects.get(id=pk)
    serviceuser = request.user.serviceuser
    template = render_to_string('profiles/booksucess_email_template.html', {'spname': serviceprovider.fullname, 'suname': serviceuser.firstname, 'service': serviceprovider.service})
    email = EmailMessage(
        'New booking',
        template,
        settings.EMAIL_HOST_USER,
        [serviceprovider.email], 
        )
    email.fail_silently=False
    email.send()
    
    context = {'serviceprovider': serviceprovider, 'serviceuser': serviceuser}
    return render(request, 'profiles/booksuccess.html', context)


@login_required(login_url='profiles:homepage')
@allowed_users(allowed_roles=['serviceprovider'])
def bookingaccepted(request, pk):
    serviceprovider = request.user.serviceprovider
    serviceuser = Serviceuser.objects.get(id=pk)
    template = render_to_string('profiles/bookingaccepted_email_template.html', {'spname': serviceprovider.fullname, 'suname': serviceuser.firstname, 'service': serviceprovider.service})
    email = EmailMessage(
        'Booking Accepted!',
        template,
        settings.EMAIL_HOST_USER,
        [serviceuser.email], 
        )
    email.fail_silently=False
    email.send()
    
    context = {'serviceprovider': serviceprovider, 'serviceuser': serviceuser}
    return render(request, 'profiles/bookingaccepted.html', context)


@login_required(login_url='profiles:homepage')
@allowed_users(allowed_roles=['serviceprovider'])
def bookingdeclined(request, pk):
    serviceprovider = request.user.serviceprovider
    serviceuser = Serviceuser.objects.get(id=pk)
    template = render_to_string('profiles/bookingdeclined_email_template.html', {'spname': serviceprovider.fullname, 'suname': serviceuser.firstname, 'service': serviceprovider.service})
    email = EmailMessage(
        'Booking Declined',
        template,
        settings.EMAIL_HOST_USER,
        [serviceuser.email], 
        )
    email.fail_silently=False
    email.send()
    
    context = {'serviceprovider': serviceprovider, 'serviceuser': serviceuser}
    return render(request, 'profiles/bookingdeclined.html', context)


@login_required(login_url='profiles:homepage')
# @allowed_users(allowed_roles=['serviceprovider'])
def bookingcanceled_sp(request, pk):
    serviceprovider = request.user.serviceprovider
    serviceuser = Serviceuser.objects.get(id=pk)
    template = render_to_string('profiles/bookingcanceledbysp_email_template.html', {'spname': serviceprovider.fullname, 'suname': serviceuser.firstname, 'service': serviceprovider.service})
    email = EmailMessage(
        'Booking Canceled by Service Provider',
        template,
        settings.EMAIL_HOST_USER,
        [serviceuser.email], 
        )
    email.fail_silently=False
    email.send()
    
    context = {'serviceprovider': serviceprovider, 'serviceuser': serviceuser}
    return render(request, 'profiles/bookingcanceledbysp.html', context)


@login_required(login_url='profiles:homepage')
# @allowed_users(allowed_roles=['serviceuser'])
def bookingcanceled_su(request, pk):
    serviceprovider = Serviceprovider.objects.get(id=pk)
    serviceuser = request.user.serviceuser
    template = render_to_string('profiles/bookingcanceledbysu_email_template.html', {'spname': serviceprovider.fullname, 'suname': serviceuser.firstname, 'service': serviceprovider.service})
    email = EmailMessage(
        'Booking Canceled by Service User',
        template,
        settings.EMAIL_HOST_USER,
        [serviceprovider.email], 
        )
    email.fail_silently=False
    email.send()
    
    context = {'serviceprovider': serviceprovider, 'serviceuser': serviceuser}
    return render(request, 'profiles/bookingcanceledbysu.html', context)


@login_required(login_url='profiles:homepage')
@allowed_users(allowed_roles=['serviceprovider', 'admin'])
def updateBookingStatus(request, pk):
    booking = Booking.objects.get(id=pk)

    if request.method == 'POST':
        print('Printing post:', request.POST)
        
        # First, you should retrieve the team instance you want to update
        booking = Booking.objects.get(id=request.POST['id'])

        # Next, you update the status
        if request.POST.get('status'):
            booking.status = request.POST.get('status')
            booking.save()
            return redirect(reverse ('profiles:serviceproviderdash'))

    context = {'booking':booking}
    return render(request,'profiles/serviceProviderDashboard.html', context)



@login_required(login_url='profiles:homepage')
@allowed_users(allowed_roles=['serviceuser'])
def serviceuserdash(request):
    bookings = request.user.serviceuser.booking_set.all()
    today_date = datetime.now().date()
    time_now = datetime.now().time()
    context = {'bookings': bookings, 'time_now':time_now, 'today_date':today_date }
    print('Printing today_date', today_date)
    print('Printing time_now', time_now)
    return render(request, 'profiles/serviceuserdash.html', context)


@login_required(login_url='profiles:homepage')
@allowed_users(allowed_roles=['serviceuser'])
def serviceUserProfile(request):
    serviceuser = request.user.serviceuser
    username = request.user
    firstname = serviceuser.firstname
    lastname = serviceuser.lastname
    gender = serviceuser.gender
    phone = serviceuser.phone
    email = serviceuser.email
    date = serviceuser.date_created
    profile_pic = serviceuser.profile_pic.url
    print('Profile',  profile_pic)
    context = {'username':username, 'firstname':firstname, 'lastname':lastname, 'gender':gender, 'phone':phone, 'email':email, 'date':date }
    return render(request, 'profiles/serviceuserProfile.html', context)

def serviceUserDetails(request, pk):
    serviceuser = Serviceuser.objects.get(id=pk)
    username = request.user
    firstname = serviceuser.firstname
    lastname = serviceuser.lastname
    gender = serviceuser.gender
    phone = serviceuser.phone
    email = serviceuser.email
    date = serviceuser.date_created
    profile_pic = serviceuser.profile_pic
    context = {'username':username, 'firstname':firstname, 'lastname':lastname, 'gender':gender, 'phone':phone, 'email':email, 'date':date}
    return render(request, 'profiles/serviceuserProfile.html', context)



@login_required(login_url='profiles:homepage')
@allowed_users(allowed_roles=['serviceuser'])
def updateServiceuser(request, pk):
    serviceuser = request.user.serviceuser
    form = ServiceuserForm(instance=serviceuser)

    if request.method == 'POST':
        form = ServiceuserForm(request.POST, request.FILES, instance=serviceuser)
        if form.is_valid():
            form.save()

       
            messages.success(request, 'Your profile was updated successfully!')
            return redirect(reverse ('profiles:profile'))

    context = {'form': form, 'serviceuser':serviceuser}
    return render(request, 'profiles/editServiceuser.html', context) 


@login_required(login_url='profiles:homepage')
@allowed_users(allowed_roles=['admin'])
def updateServiceprovider(request, pk):
    
    serviceprovider = Serviceprovider.objects.get(id=pk)
    form = ServiceproviderForm(instance=serviceprovider)

    if request.method == 'POST':
        form = ServiceproviderForm(request.POST,request.FILES, instance=serviceprovider)
        if form.is_valid():
            form.save()
            return redirect(reverse ('profiles:dashboard'))

    context = {'form': form}
    return render(request, 'profiles/serviceprovider.html', context) 


@login_required(login_url='profiles:homepage')
@allowed_users(allowed_roles=['admin'])
def deleteServiceuser(request, pk):
    serviceusers = ServiceuserModel.objects.get(id=pk)
    if request.method == "POST":
        serviceusers.delete()
        return redirect(reverse ('profiles:dashboard'))
    context = {'item': serviceusers}
    return render(request, 'profiles/deleteServiceuser.html', context) 


@login_required(login_url='profiles:homepage')
@allowed_users(allowed_roles=['admin'])
def deleteServiceprovider(request, pk):
    serviceprovider = Serviceprovider.objects.get(id=pk)
    if request.method == "POST":
        serviceprovider.delete()
        return redirect(reverse ('profiles:dashboard'))
    context = {'item': serviceprovider}
    return render(request, 'profiles/deleteServiceprovider.html', context) 

 
@login_required(login_url='profiles:homepage')
@allowed_users(allowed_roles=['serviceprovider'])
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
    # captioners = Serviceprovider.objects.service.Captioning.all()
    context = {'serviceproviders': serviceproviders, }
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
@allowed_users(allowed_roles=['serviceuser', 'admin'])
def tactileInterpList(request):
	serviceproviders = Serviceprovider.objects.all()
	context = {'serviceproviders': serviceproviders}
	return render(request, 'profiles/splist/tactileInterpreter.html', context)


@login_required(login_url='profiles:homepage')
@allowed_users(allowed_roles=['serviceuser', 'admin'])
def spList(request):
    serviceproviders = Serviceprovider.objects.all()
    context = {'serviceproviders': serviceproviders}
    return render(request, 'profiles/splist/allServiceProviders.html', context)
