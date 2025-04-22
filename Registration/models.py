from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    user_type = models.CharField(max_length=10, default="nothing")
    is_verified = models.BooleanField(default=False)  

   

    def __str__(self):
        return self.user.username
class BidderPofile(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100, default="")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default="")
    qualifications = models.CharField(max_length=200, default="")
    experience = models.PositiveIntegerField(default=0)
    contact_number = models.CharField(max_length=15, default="")
    email = models.EmailField(default="")
    address = models.CharField(max_length=100, default="")
    biography = models.TextField(default="")
    profile_pic = models.ImageField(upload_to='bidder_profile_pics/', default="default.jpg")
    latitude = models.CharField(max_length=100,default="0000")
    longitude = models.CharField(max_length=100,default="0000")
    @property
    def __str__(self):
        return self.user.username
    
class PatientProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    )

    address = models.CharField(max_length=100, default="")
    phone_number = models.CharField(max_length=20, default="")
    occupation = models.CharField(max_length=100, default="")
    age = models.PositiveIntegerField(default=0)
    profile_pic = models.ImageField(upload_to='profile_pics/', default="default.jpg")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default="")
    city = models.CharField(max_length=100,default="Unknown")
    state = models.CharField(max_length=100,default="AZ")
    zip_code = models.CharField(max_length=100,default="Unknown")

    def __str__(self):
        return self.user.username
        
