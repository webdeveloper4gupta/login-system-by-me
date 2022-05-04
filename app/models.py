from django.db import models

# Create your models here.
class booking(models.Model):
    name=models.CharField(max_length=90)
    fromto=models.CharField(max_length=89)
    destination=models.CharField(max_length=89)
    phno=models.CharField(max_length=10)
    email=models.EmailField(max_length=90,default=None)
    userid=models.CharField(max_length=90,default=None)

    