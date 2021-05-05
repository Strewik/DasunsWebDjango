from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import *

def create_serviceuser(sender,instance,created, **kwargs):
    if created:
        Serviceuser.objects.create(user=instance)
        print("profile created")
        
post_save.connect(create_serviceuser, sender=User)

def update_serviceuser(sender,instance, created, **kwargs):
    if created == False:
        instance.serviceuser.save()
        print("profile updated")
        
post_save.connect(update_serviceuser, sender=User)          
        