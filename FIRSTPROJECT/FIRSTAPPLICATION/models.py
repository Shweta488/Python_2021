from django.db import models

# Create your models here.
#Name, ID, Contact, Address

class Information(models.Model):
    name = models.CharField(max_length=(15))
    id = models.IntegerField(unique=True, primary_key= True)
    contact = models.IntegerField(unique=True)
    address = models.CharField(max_length=(200), blank=True)
