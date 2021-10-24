from django.db import models


class product(models.Model):
    name = models.CharField(max_length=50)
    buy_price = models.DecimalField(decimal_places=14, max_digits=1000)
    sell_price = models.DecimalField(decimal_places=14, max_digits=1000)