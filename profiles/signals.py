from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from .models import Serviceuser, Serviceprovider


def create_serviceuser_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='serviceuser')
        instance.groups.add(group) # instance is the user
        Serviceuser.objects.create(
                user=instance,
                email=instance.email,
                firstname=instance.firstname,
                lastname=instance.lastname,
                phone=instance.phone
            )
        print('Su profile created!')

post_save.connect(create_serviceuser_profile, sender=User)

