from django.db import models

class location(models.Model):
    geo_location_x = models.CharField(max_length=1000)
    geo_location_y = models.CharField(max_length=1000)