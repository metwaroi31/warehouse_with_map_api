from django.db import models
from django.db.models.fields import CharField
# from warehouse_map_api.models.product impor

class bill(models.Model):
    price = models.DecimalField(decimal_places=14, max_digits=1000)
    received_date = models.CharField(max_length=1000)
    # bill_detail = models.ForeignKey(bill_product, related_name="bill_detail", on_delete=models.CASCADE)


