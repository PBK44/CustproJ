from django.db import models

# Create your models here.
class Customer(models.Model):
    cid=models.IntegerField()
    cname=models.CharField(max_length=30)
    Accno=models.IntegerField()
    bank=models.CharField(max_length=30)
    branch=models.CharField(max_length=30)
    
