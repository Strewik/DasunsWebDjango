from django.forms import ModelForm
from .models import *


class ServiceuserForm(ModelForm):
    class Meta:
        model = Serviceuser
        fields = '__all__' 