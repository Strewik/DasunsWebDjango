from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput
from django.core import validators
from django.forms import ValidationError

def check_size(value):
	if len(value) < 3:
		raise forms.ValidationError(" Username required,  3 to 150 characters. Letters, digits and @/./+/-/_ only.")


GENDER = (
(None, 'Select your gender'),
('male', 'male'),
('female', 'female'),
)
class CreateUserForm(UserCreationForm):
	username = forms.CharField(max_length=50,  validators= [check_size,], widget=forms.TextInput(attrs={'id':'username', 'name':'username', 'placeholder': 'User Name e.g kente', 'class': 'form-control'}))
	firstname = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'id':'firstname','name':'firstname','placeholder': 'First Name', 'class': 'form-control'}))
	lastname = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'id':'lastname','placeholder': 'Last Name', 'class': 'form-control'}))
	gender = forms.ChoiceField(choices=GENDER, widget=forms.Select(attrs={'id':'gender','class': 'form-control'}))
	phone = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'id':'phone','placeholder': 'Phone Number', 'class': 'form-control'}))
	email = forms.EmailField(max_length=50, widget=forms.TextInput(attrs={'id':'email','placeholder': 'Email', 'class': 'form-control'}))
	password1 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'id':'password1','placeholder': 'Create Password', 'class': 'form-control'}))
	password2 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'id':'password2','placeholder': 'Confrim Password', 'class': 'form-control'}))
	
	def clean_email(self):
		if User.objects.filter(email=self.cleaned_data['email']).exists():
			raise forms.ValidationError("The given email is already registered")
		return self.cleaned_data['email']
	
		email = self.cleaned_data['email']

		if not email:
			raise ValidationError('Email is required')
		return email
	


	class Meta:
		model = User
		fields = ("username", "firstname", "lastname", "gender", "phone", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(CreateUserForm, self).save(commit=False)
		user.firstname = self.cleaned_data['firstname']
		user.lastname = self.cleaned_data['lastname']
		user.gender = self.cleaned_data['gender']
		user.phone = self.cleaned_data['phone']
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user


class ServiceuserForm(ModelForm):
	class Meta:
		model = Serviceuser
		fields = '__all__'
		exclude=['user']


DAY = (('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'),
	('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday'))

class ServiceproviderForm(ModelForm):
	class Meta:
		model = Serviceprovider
		fields = '__all__'
		exclude=['user']
		# services = forms.ModelMultipleChoiceField(queryset=Service.objects.all(),widget=forms.CheckboxSelectMultiple)


		# av = forms.ModelMultipleChoiceField(
		# queryset=Day.objects.all(),
		# widget=forms.CheckboxSelectMultiple
		# 	)

		labels = {
			'fullname':'Fullname',
			'phone':'Phone number',
			'email':'Email',
			'nin':'NIN',
			'dob':'Date of birth',
		# 	'gender':'Gender',
			'phyadd':'Physical address',
		# 	'yearexp':'At least one year of experience',
		# 	'notmidman':'Not a middleware',
		# 	'skillset':'I have the skillset',
		# 	'internet':'Device with an active connection',
			'qualification':'Train certification',
			'portifolio':'Portifolio link',
			'profession':'About me',
			'ref1name':'Ref 1 name',
			'ref1title':'Ref 1 title',
			'ref1email':'Ref 1 email',
			'ref1phone':'Ref 1 phone number',
			'ref2name':'Ref 2 name',
			'ref2title':'Ref 2 title',
			'ref2email':'Ref 2 email',
			'ref2phone':'Ref 2 phone number',
		# 	'service':'Service',
		# 	'availability':'Availability',
		# 	'status':'Status',
		# 	'starttime':'Start time',
		# 	'endtime':'End time',
		# 	'pricevisit':'Price per  visit',
		# 	'terms':'Terms'
		}

		widgets = {
			'fullname':forms.TextInput(attrs={'class':'form-control'}),
			'phone':forms.TextInput(attrs={'class':'form-control'}),
			'email':forms.TextInput(attrs={'class':'form-control'}),
			'nin':forms.TextInput(attrs={'class':'form-control'}),
			'dob':forms.TextInput(attrs={'class':'form-control'}),
			'gender':forms.Select(attrs={'class':'form-control'}),
			'phyadd':forms.TextInput(attrs={'class':'form-control'}),
			'yearexp':forms.TextInput(attrs={'class':'form-control'}),
			'notmidman':forms.TextInput(attrs={'class':'form-control'}),
			'skillset':forms.TextInput(attrs={'class':'form-control'}),
			'internet':forms.TextInput(attrs={'class':'form-control'}),
			'qualification':forms.FileField(),
			'portifolio':forms.TextInput(attrs={'class':'form-control'}),
			'profession':forms.TextInput(attrs={'class':'form-control'}),
			'ref1name':forms.TextInput(attrs={'class':'form-control'}),
			'ref1title':forms.TextInput(attrs={'class':'form-control'}),
			'ref1email':forms.TextInput(attrs={'class':'form-control'}),
			'ref1phone':forms.TextInput(attrs={'class':'form-control'}),
			'ref2name':forms.TextInput(attrs={'class':'form-control'}),
			'ref2title':forms.TextInput(attrs={'class':'form-control'}),
			'ref2email':forms.TextInput(attrs={'class':'form-control'}),
			'ref2phone':forms.TextInput(attrs={'class':'form-control'}),
			'service':forms.Select(attrs={'class':'form-control'}),
			'availability':forms.CheckboxSelectMultiple(choices=DAY),
			'status':forms.Select(attrs={'class':'form-control'}),
			'starttime':forms.TextInput(attrs={'class':'form-control'}),
			'endtime':forms.TextInput(attrs={'class':'form-control'}),
			'pricevisit':forms.TextInput(attrs={'class':'form-control'}),
			'terms':forms.TextInput(attrs={'class':'form-control'})
		}
        
        
class BookingForm(ModelForm):
	class Meta:
		model = Booking
		fields = '__all__'
		exclude = ('status',)
		labels  = {
			'name':'Full Name', 
			'phone':'Phone No.', 
			'email':'Email', 
			'meetplace':'Meeting Place', 
			'meetdate':'Meeting Date',
			'starttime':'Start Time',
			'endtime':'End Time',
			'serviceuser':'Service User',
			'serviceprovider':'Service Provider'
			}
		widgets = {
			'name': forms.TextInput(attrs={'placeholder': 'Enter your Full name','class':'form-control'}),
			'phone': forms.TextInput(attrs={'placeholder': 'Enter your phone number','class':'form-control'}),
			'email': forms.TextInput(attrs={'placeholder': 'Enter your Email address','class':'form-control'}),
			'meetplace': forms.TextInput(attrs={'placeholder': 'Preferred meeting place','class':'form-control'}),
			'meetdate': DatePickerInput(attrs={'placeholder': 'Schedule your preferred date','class':'form-control'}),
			'starttime': TimePickerInput(attrs={'placeholder': 'Enter Starting time','class':'form-control'}),
			'endtime': TimePickerInput(attrs={'placeholder': 'Enter Ending time','class':'form-control'}),
			'serviceuser': forms.TextInput(attrs={'placeholder': 'Select service user','class':'form-control'}),
			'serviceprovider': forms.TextInput(attrs={'placeholder': 'Select service provider','class':'form-control'}),
		} 
