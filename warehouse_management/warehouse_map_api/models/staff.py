from django.db import models
from warehouse_map_api.models.location import location

class staff(models.Model):
    name = models.CharField(max_length=50)
    # location = models.ForeignKey(location, related_name='location', on_delete=models.CASCADE)
    