from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    USER_TYPE_CHOICES = (
        ('citizen', 'Citizen'),
        ('agency', 'Government Agency'),
        ('npc', 'NPC'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='citizen')
    district = models.CharField(max_length=100, blank=True)
    province = models.CharField(max_length=100, blank=True)
    gender = models.CharField(max_length=10, blank=True)
    primary_id = models.CharField(max_length=100, blank=True)

class Need(models.Model):
    description = models.TextField()
    agency = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'user_type': 'agency'})
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Contract(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    npc = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'user_type': 'npc'})
    status = models.CharField(max_length=20, default='advertised')
    created_at = models.DateTimeField(auto_now_add=True)