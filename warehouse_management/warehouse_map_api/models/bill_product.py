from django.db import models
from warehouse_map_api.models.bill import bill
from warehouse_map_api.models.product import Product

class bill_product(models.Model):
    bill = models.ForeignKey(bill, related_name="bill", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name="product", on_delete=models.CASCADE)
    qty = models.DecimalField(decimal_places=0, max_digits=1000)
    