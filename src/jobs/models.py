from django.db import models

# Create your models here.
class Job(models.Model):
		id = models.AutoField(primary_key=True, editable=False) # max_length = required
		job_type = models.CharField(max_length = 100)
		job_prioity = models.CharField(max_length = 100)
		order_number = models.CharField(max_length = 100)
		invoice_number = models.CharField(max_length = 100)
		due_date = models.DateField()
		assigned = models.CharField(max_length = 100)
		status = models.CharField(max_length = 100)
		date_created = models.DateField(auto_now_add = True)
		last_mod_date = models.DateField(auto_now = True)
		
class Meta:
		indexes = [
		models.Index(fields=['order_number', 'invoice_number'], name = 'job_index'),
		]