from django.db import models

# Create your models here.

class Trades(models.Model):
    position_types = [('long', 'Long'),('short', 'Short')]
    exchange = models.CharField(max_length=100)
    market = models.CharField(max_length=100)
    position = models.CharField(max_length=5, choices=position_types)
    open_price = models.FloatField(null=True)
    close_price = models.FloatField(null=True)
    amount = models.FloatField(null=True)