from datetime import date
from ntpath import join
from django.db import models

# Create your models here.

class User(models.Model):

    name = models.CharField(max_length=50,null=True)
    email = models.EmailField(unique=True,null=True)
    password = models.CharField(max_length=25,null=True)
    address = models.TextField(null= True)
    mobile = models.CharField(max_length=50,null=True)
    doj = models.DateField(null=True)
    pic = models.ImageField(upload_to='Profile Pic',default='avtar.png')

    def __str__(self):
        return self.email
          
        