from django.db import models

class position(models.Model):
    name = models.CharField(max_length=50)