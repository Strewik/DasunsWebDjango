from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput

class CreateUserForm(UserCreationForm):
	username = forms.CharField(max_length=254,required=True, widget=forms.TextInput(attrs={'placeholder': 'User Name', 'class': 'form-control'}))
	# firstname = forms.CharField(max_length=254,required=True, widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}))
	# lastname = forms.CharField(max_length=254,required=True, widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'}))
	email = forms.EmailField(max_length=254,required=True, widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}))
	password1 = forms.CharField(max_length=254,required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Create Password', 'class': 'form-control'}))
	password2 = forms.CharField(max_length=254,required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Confrim Password', 'class': 'form-control'}))
	
	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")
		# fields = ("username", "firstname", "lastname", "email", "password1", "password2")
		
	def save(self, commit=True):
		user = super(CreateUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

class ServiceuserForm(ModelForm):
	class Meta:
		model = Serviceuser
		fields = '__all__'
		exclude=['user']
		# fields = ('name', 'phone', 'email')
		# labels  = {
		# 	'name':'Full Name', 
		# 	'phone':'Phone No.', 
		# 	'email':'Email', 
		# 	}
		# widgets = {
		# 	'name': forms.TextInput(attrs={'placeholder': 'Enter your Full name','class':'form-control'}),
		# 	'phone': forms.TextInput(attrs={'placeholder': 'Enter your phone number','class':'form-control'}),
		# 	'email': forms.TextInput(attrs={'placeholder': 'Enter your Email address','class':'form-control'}),

		# }


class ServiceproviderForm(ModelForm):
    class Meta:
        model = Serviceprovider
        fields = '__all__' 
        
        
class BookingForm(ModelForm):
	class Meta:
		model = Booking
		fields = ('name', 'phone', 'email', 'meetplace', 'meetdate','starttime', 'endtime')
		labels  = {
			'name':'Full Name', 
			'phone':'Phone No.', 
			'email':'Email', 
			'meetplace':'Meeting Place', 
			'meetdate':'Meeting Date',
			'starttime':'Start Time',
			'endtime':'End Time',
			# 'serviceuser':'Service User',
			# 'user': 'Service User',
			# 'serviceprovider':'Service Provider'
			}
		widgets = {
			'name': forms.TextInput(attrs={'placeholder': 'Enter your Full name','class':'form-control'}),
			'phone': forms.TextInput(attrs={'placeholder': 'Enter your phone number','class':'form-control'}),
			'email': forms.TextInput(attrs={'placeholder': 'Enter your Email address','class':'form-control'}),
			'meetplace': forms.TextInput(attrs={'placeholder': 'Preferred meeting place','class':'form-control'}),
			'meetdate': DatePickerInput(attrs={'placeholder': 'Schedule your preferred date','class':'form-control'}),
			'starttime': TimePickerInput(attrs={'placeholder': 'Enter Starting time','class':'form-control'}),
			'endtime': TimePickerInput(attrs={'placeholder': 'Enter Ending time','class':'form-control'}),
			# 'serviceuser': forms.TextInput(attrs={'placeholder': 'Select service user','class':'form-control'}),
			# 'user': forms.TextInput(attrs={'readonly': 'readonly'}),
			# 'serviceprovider': forms.TextInput(attrs={'placeholder': 'Select service provider','class':'form-control'}),
		} 

