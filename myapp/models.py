from django.db import models

# Create your models here.

class Profile(models.Model):

    name = models.CharField(max-len=30)
    age= models.IntegerField()
    address = models.TextField()
    image = models.ImageField()
    