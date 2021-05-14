import django_filters
from .models import *
from django_filters import CharFilter

class BookingFilter(django_filters.FilterSet):
    class Meta:
        model = Booking
        fields = '__all__'


class ServiceproviderFilter(django_filters.FilterSet):
    fullname = CharFilter(field_name='fullname', lookup_expr='icontains')
    phyadd = CharFilter(field_name='phyadd', lookup_expr='icontains')
    class Meta:
        model = Serviceprovider
        fields = ('fullname', 'phyadd', 'service')

class ServiceuserFilter(django_filters.FilterSet):
    user = CharFilter(field_name='user', lookup_expr='icontains')
    firstname = CharFilter(field_name='firstname', lookup_expr='icontains')
    lastname = CharFilter(field_name='lastname', lookup_expr='icontains')
    class Meta:
        model = Serviceuser 
        fields = ('user', 'firstname', 'lastname')
        
        