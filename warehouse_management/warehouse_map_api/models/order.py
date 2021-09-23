from django.db import models
from django.db.models.fields import CharField
from warehouse_map_api.models.location import location
from warehouse_map_api.models.staff import staff
from warehouse_map_api.models.warehouse import warehouse

class order(models.Model):
    staff = models.ForeignKey(staff, related_name="staff", on_delete=models.CASCADE)
    directions = models.CharField(max_length=1000)
    location = models.ForeignKey(location, related_name='location', on_delete=models.CASCADE)
    warehouse = models.ForeignKey(warehouse, related_name='warehouse', on_delete=models.CASCADE)
    