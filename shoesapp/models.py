import email
from msilib.schema import Class
from unicodedata import name
from django.db import models

# Create your models here.

# class product(models.Model):
     
#     name = models.CharField(max_length=50)
#     price = models.IntegerField(default=0)
#     description= models.CharField(max_length=200,default='')
#     image = models.ImageField(upload_to='product pic',default='avtar.png')

# class Category(models.Model):
#     name = models.CharField(max_length=20)
#     def __str__(self):
#         return self.name

class Register(models.Model):
    name=models.CharField(max_length=20)
    mobile=models.CharField(max_length=13)
    gender=models.CharField(max_length=6)
    email=models.EmailField(unique=True)
    address=models.TextField(max_length=60)
    password=models.CharField(max_length=20)
    pic=models.ImageField(upload_to='Profile Pic',default="avtar.png")

    def __str__(self):
        return self.name


