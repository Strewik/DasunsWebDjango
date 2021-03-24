from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *
from bootstrap_datepicker_plus import DatePickerInput, TimePickerInput, DateTimePickerInput, MonthPickerInput

class CreateUserForm(UserCreationForm):
	username = forms.CharField(max_length=254,required=True, widget=forms.TextInput(attrs={'placeholder': 'User Name', 'class': 'form-control'}))
	email = forms.EmailField(max_length=254,required=True, widget=forms.TextInput(attrs={'placeholder': 'Email', 'class': 'form-control'}))
	password1 = forms.CharField(max_length=254,required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Create Password', 'class': 'form-control'}))
	password2 = forms.CharField(max_length=254,required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Confrim Password', 'class': 'form-control'}))
	
	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")
		
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

class BookingForm(ModelForm):
	class Meta:
		model = Booking
		fields = ('name', 'phone', 'email', 'meetplace', 'meetdate','starttime', 'endtime', 'serviceuser', 'serviceprovider')
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
			'serviceuser': forms.Select(attrs={'placeholder': 'Select service user','class':'form-control'}),
			'serviceprovider': forms.Select(attrs={'placeholder': 'Select service provider','class':'form-control'}),
		} 


# from django import forms

# class ContactForm(forms.Form):
#     name = forms.CharField(max_length=30)
#     email = forms.EmailField(max_length=254)
#     message = forms.CharField(
#         max_length=2000,
#         widget=forms.Textarea(),
#         help_text='Write here your message!'
#     )
#     source = forms.CharField(       # A hidden input for internal use
#         max_length=50,              # tell from which page the user sent the message
#         widget=forms.HiddenInput()
#     )

#     def clean(self):
#         cleaned_data = super(ContactForm, self).clean()
#         name = cleaned_data.get('name')
#         email = cleaned_data.get('email')
#         message = cleaned_data.get('message')
#         if not name and not email and not message:
#             raise forms.ValidationError('You have to write something!')


# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User


# # Create your forms here.

# class SignUpForm(UserCreationForm):
# 	email = forms.EmailField(max_length=254,required=True)

# 	class Meta:
# 		model = User
# 		fields = ("username", "email", "password1", "password2")

# 	def save(self, commit=True):
# 		user = super(SignUpForm, self).save(commit=False)
# 		user.email = self.cleaned_data['email']
# 		if commit:
# 			user.save()
# 		return user
