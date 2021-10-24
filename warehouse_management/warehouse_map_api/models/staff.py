from django.db import models
from warehouse_map_api.models.position import position

class staff(models.Model):
    name = models.CharField(max_length=50)
    position = models.ForeignKey(position, related_name='position', on_delete=models.CASCADE)
    