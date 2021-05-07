from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Serviceuser(models.Model):
<<<<<<< HEAD
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=200, null=True)
    lastname = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(default="profile.png", null=True, blank=True)
=======
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    profile_pic = models.ImageField(default="profile.png", blank=True)
>>>>>>> a08ce6ac4994805e5a3732a5fee4d75560a9c7c7
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.firstname)
    #    return "%s %s" % (self.first_name, self.last_name)

class Serviceprovider(models.Model):
    GENDER = (('Male', 'Male'), ('Female', 'Female'))
    SERVICE = (('Personal Support Assistance', 'Personal Support Assistance'),
    ('Ugandan Sign Language Interpreter', 'Ugandan Sign Language Interpreter'),
    ('International Sign Language Interpreter', 'International Sign Language Interpreter'), 
    ('Captioning', 'Captioning'), ('Mobility Guide', 'Mobility Guide'),)
    STATUS = (('Pending', 'Pending'), ('Active', 'Active'), ('Suspended', 'Suspended'),)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, unique=True)
    nin = models.CharField(max_length=200)
    dob = models.CharField(max_length=200)
    gender = models.CharField(max_length=200, choices=GENDER,)
    phyadd = models.CharField(max_length=200)
    yearexp = models.CharField(max_length=200)
    notmidman = models.CharField(max_length=200)
    skillset = models.CharField(max_length=200)
    internet = models.CharField(max_length=200)
    qualification = models.FileField()
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
    service = models.CharField(max_length=200, choices=SERVICE)
<<<<<<< HEAD
    availability = models.CharField(max_length=200, null=True)
=======
    availability = models.CharField(max_length=200)
>>>>>>> a08ce6ac4994805e5a3732a5fee4d75560a9c7c7
    status = models.CharField(max_length=200, choices=STATUS,)
    starttime = models.CharField(max_length=200) 
    endtime = models.CharField(max_length=200)
    pricevisit = models.CharField(max_length=200)
    terms = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    objects=models.Manager()
    

    def __str__(self):
        return str(self.fullname)
    
    class Meta:
        ordering = ['-date_created','fullname']

class Booking(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    meetplace = models.CharField(max_length=200)
    meetdate = models.CharField(max_length=200)
    starttime = models.CharField(max_length=200)
    endtime = models.CharField(max_length=200)
    serviceuser = models.ForeignKey(Serviceuser, null=True, on_delete=models.SET_NULL)
<<<<<<< HEAD
    serviceprovider = models.ForeignKey(Serviceprovider,null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True,)
    status = models.CharField(max_length=200, default="Pending")
=======
    serviceprovider = models.ForeignKey(Serviceprovider, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200, default="Pending", blank=True)
>>>>>>> a08ce6ac4994805e5a3732a5fee4d75560a9c7c7
   

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['-date_created','name']       
    # @property
    # def service_hours(self):
    #     return int(self.endtime - self.starttime)
        
