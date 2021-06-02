from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField


# Create your models here.

class Serviceuser(models.Model):
    GENDER = (('Male', 'Male'), ('Female', 'Female'))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    gender = models.CharField(max_length=200, choices=GENDER, null=True)
    profile_pic = models.ImageField(upload_to='profilepics/', default="profile.png", blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return "%s %s" % (self.firstname, self.lastname)
    class Meta:
        ordering = ['-date_created','firstname' ] 

    
class Serviceprovider(models.Model):
    GENDER = (('Male', 'Male'), ('Female', 'Female'))
    SERVICE = (('Personal Support Assistance', 'Personal Support Assistance'),
               ('Ugandan Sign Language Interpreter',
                'Ugandan Sign Language Interpreter'),
               ('International Sign Language Interpreter',
                'International Sign Language Interpreter'),
               ('Captioning', 'Captioning'), ('Mobility Guide', 'Mobility Guide'),
               ('Tactile Sign Language Interpreter', 'Tactile Sign Language Interpreter'),)
    
    STATUS = (('Pending', 'Pending'), ('Active', 'Active'),
              ('Suspended', 'Suspended'),)
    
    DAY = (('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'),
           ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday'))
    
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
    service = MultiSelectField(max_length=200, choices=SERVICE)
    availability = MultiSelectField(max_length=200, choices=DAY)
    status = models.CharField(max_length=200, choices=STATUS,)
    starttime = models.TimeField(max_length=200) 
    endtime = models.TimeField(max_length=200)
    pricevisit = models.CharField(max_length=200)
    terms = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

    def __str__(self):
        return str(self.fullname)

    class Meta:
        ordering = ['-date_created', 'fullname']
        
class Booking(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    meetplace = models.CharField(max_length=200)
    meetdate = models.DateField(max_length=200)
    starttime = models.TimeField(max_length=200)
    endtime = models.TimeField(max_length=200)
    serviceuser = models.ForeignKey(Serviceuser, null=True, on_delete=models.SET_NULL)
    serviceprovider = models.ForeignKey(Serviceprovider, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200, default="Pending", blank=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['-date_created', 'name']

class Rating(models.Model):
    star = models.IntegerField(blank=True)
    comment = models.CharField(max_length=256, blank=True)
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
        
    def __str__(self):
        return str(self.booking.name)
    
    
