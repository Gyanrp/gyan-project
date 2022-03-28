from django.db import models

# Create your models here.

class product(models.Model):
     
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    description= models.CharField(max_length=200,default='')
    image = models.ImageField(upload_to='product pic',default='avtar.png')

class Category(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name





