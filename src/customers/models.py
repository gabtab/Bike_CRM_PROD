from django.db import models

# Create your models here.
class Customer(models.Model):
	name = models.CharField(max_length=80)
	bike = models.CharField(max_length=100)
	