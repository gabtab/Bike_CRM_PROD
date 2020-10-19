from django.db import models

# Create your models here.
class Bike(models.Model):
		id = models.AutoField(primary_key=True, editable=False) # max_length = required
		Bike_make = models.CharField(max_length = 100)
		Bike_model = models.CharField(max_length = 100)
		Bike_year = models.CharField(max_length = 100)
		
class Meta:
		indexes = [
		models.Index(fields=['Bike_make', 'Bike_model'], name = 'bike_index'),
		]