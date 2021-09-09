from django.db import models
from warehouse_map_api.models.location import location

class warehouse(models.Model):
    brand_name = models.CharField(max_length=50)
    location = models.ForeignKey(location, on_delete=models.CASCADE)
    