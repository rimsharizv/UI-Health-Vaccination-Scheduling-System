from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from core.models import AbstractBaseModel

# Create your models here.
ROLE_CHOICES = (
    ("admin", "Admin"),
    ("nurse", "Nurse"),
    ("patient", "Patient"),
  
)

GENDER_CHOICES = (
    ("Male", "Male"),
    ("Female", "Female"),
    ("Other", "Other"),
)

RACE_CHOICES = (
    ("Black or African", "Black or African"),
    ("White", "White"),
    ("Caucasian", "Caucasian"),
    ("Spanish or Latino", "Spanish or Latino"),
)

class User(AbstractUser, AbstractBaseModel):
    role = models.CharField(choices=ROLE_CHOICES, max_length=32, null=True)
    
    def __str__(self):
        return self.username

    def name(self):
        return f"{self.first_name} {self.last_name}"



class Nurse(AbstractBaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    employeeId = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES)
    phone_number =models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    age = models.IntegerField(null=True)


    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class Patient(AbstractBaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    social_security_number = models.CharField(max_length=255)
    race = models.CharField(max_length=255, choices=RACE_CHOICES)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES)
    phone_number =models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    age = models.IntegerField(null=True)
    occupation = models.CharField(max_length=255)
    medical_history = models.TextField(null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
