from django.db import models
from warehouse_map_api.models.product import Product

class order_product(models.Model):
    order = models.IntegerField()
    product = models.ForeignKey(Product, related_name="product", on_delete=models.CASCADE)
    qty = models.DecimalField(decimal_places=0, max_digits=1000)
    