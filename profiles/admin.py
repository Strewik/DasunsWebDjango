from django.contrib import admin

from .models import Booking
from .models import Serviceprovider
from .models import Serviceuser

# Register your models here.

admin.site.register(Serviceuser)
admin.site.register(Serviceprovider)
admin.site.register(Booking)

