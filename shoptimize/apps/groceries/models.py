from django.db import models
from decimal import Decimal


class GroceryItem(models.Model):
    name = models.CharField(max_length=32)


class GroceryStore(models.Model):
    name = models.CharField(max_length=32, unique=True)


class GroceryDiscount(models.Model):
    item = models.ForeignKey(to=GroceryItem, on_delete=models.CASCADE)
    store = models.ForeignKey(to=GroceryStore, on_delete=models.CASCADE)
    price_before = models.DecimalField(max_digits=8, decimal_places=2)
    price_after = models.DecimalField(max_digits=8, decimal_places=2)

    @property
    def percent(self):
        return round(1 - self.price_after / self.price_before, 2) * 100

    @property
    def amount(self):
        return round(self.price_before - self.price_after, 2)
