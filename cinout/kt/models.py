

# Create your models here.
# Create your models here.
from datetime import datetime
from django.db import models
from django.utils import timezone





class Signup(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    dob=models.CharField(max_length=100)
    D_T= models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username



class Term(models.Model):
    details = models.CharField(max_length=500)
    last_updated_at = models.CharField(max_length=50)
