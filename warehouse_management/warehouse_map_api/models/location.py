from django.db import models

class location(models.Model):
    geo_location_x = models.DecimalField(decimal_places=14, max_digits=1000)
    geo_location_y = models.DecimalField(decimal_places=14, max_digits=1000)