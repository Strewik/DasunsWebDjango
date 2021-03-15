from django.contrib import admin

# Register your models here.

from .models import Booking
from .models import Serviceprovider
from .models import Serviceuser

admin.site.register(Serviceuser)
admin.site.register(Serviceprovider)
admin.site.register(Booking)

