from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Serviceuser(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class Serviceprovider(models.Model):
    GENDER = (('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other'),)
    SERVICE = (('Personal Support Assistance', 'Personal Support Assistance'),
    ('Ugandan Sign Language Interpreter', 'Ugandan Sign Language Interpreter'),
    ('International Sign Language Interpreter', 'International Sign Language Interpreter'), 
    ('Captioning', 'Captioning'),
    ('Mobility Guide', 'Mobility Guide'),)
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    nin = models.CharField(max_length=200)
    dob = models.CharField(max_length=200)
    gender = models.CharField(max_length=200, choices=GENDER)
    phyadd = models.CharField(max_length=200)
    yearexp = models.CharField(max_length=200)
    notmidman = models.CharField(max_length=200)
    skillset = models.CharField(max_length=200)
    internet = models.CharField(max_length=200)
    qualification = models.CharField(max_length=200)
    portifolio = models.CharField(max_length=200, blank=True)
    profession = models.CharField(max_length=200)
    ref1name = models.CharField(max_length=200)
    ref1title = models.CharField(max_length=200)
    ref1email = models.EmailField(max_length=200)
    ref1phone = models.CharField(max_length=200)
    ref2name = models.CharField(max_length=200)
    ref2title = models.CharField(max_length=200)
    ref2email = models.EmailField(max_length=200)
    ref2phone = models.CharField(max_length=200)
    service = models.CharField(max_length=200, choices=SERVICE, null=True)
    availability = models.CharField(max_length=200, null=True)
    # sunday = models.CharField(max_length=200, null=True)
    # monday = models.CharField(max_length=200, null=True)
    # tuesday = models.CharField(max_length=200, null=True)
    # wednesday = models.CharField(max_length=200, null=True)
    # thursday = models.CharField(max_length=200, null=True)
    # friday = models.CharField(max_length=200, null=True)
    # saturday = models.CharField(max_length=200, null=True)
    starttime = models.CharField(max_length=200)
    endtime = models.CharField(max_length=200)
    pricevisit = models.CharField(max_length=200, blank=True)
    terms = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.service

class Booking(models.Model):
    # STATUS = (('Pending', 'Pending'), ('Ongoing', 'Ongoing'),
    #           ('Completed', 'Completed'), ('Cancelled', 'Cancelled'))
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    meetplace = models.CharField(max_length=200, null=True)
    meetdate = models.CharField(max_length=200, null=True)
    starttime = models.CharField(max_length=200, null=True)
    endtime = models.CharField(max_length=200, null=True)
    serviceuser = models.ForeignKey(Serviceuser, null=True, on_delete=models.SET_NULL)
    serviceprovider = models.ForeignKey(Serviceprovider, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    # status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return self.serviceprovider.service
