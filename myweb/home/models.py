from django.db import models

# Create your models here.
class hey (models.Model) :
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

class hello (models.Model) :
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)    