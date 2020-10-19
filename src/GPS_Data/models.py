from django.db import models

# Create your models here.
class GPS_DATA(models.Model):
    timestamp = models.DateTimeField()
    position_lat = models.DecimalField(max_digits = 20, decimal_places = 15)
    position_long = models.DecimalField(max_digits = 20, decimal_places = 15)
    distance = models.DecimalField(max_digits = 20, decimal_places = 15)
    enhanced_altitude = models.DecimalField(max_digits = 20, decimal_places = 15)
    altitude = models.DecimalField(max_digits = 20, decimal_places = 15)
    enhanced_speed = models.DecimalField(max_digits = 20, decimal_places = 15)
    speed = models.DecimalField(max_digits = 20, decimal_places = 15)
    heart_rate = models.DecimalField(max_digits = 20, decimal_places = 15)
    cadence = models.DecimalField(max_digits = 20, decimal_places = 15)
    fractional_cadence = models.DecimalField(max_digits = 20, decimal_places = 15)
    temperature = models.DecimalField(max_digits = 20, decimal_places = 15)
    created = models.DateTimeField(auto_now_add=True)
