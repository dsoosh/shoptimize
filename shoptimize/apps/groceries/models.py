from django.db import models


class GroceryItem(models.Model):
    name = models.CharField(max_length=32)


class GroceryStore(models.Model):
    name = models.CharField(max_length=32, unique=True)


class GroceryDiscount(models.Model):
    item = models.ForeignKey(to=GroceryItem, on_delete=models.CASCADE)
    store = models.ForeignKey(to=GroceryStore, on_delete=models.CASCADE)
    price_before = models.DecimalField(max_digits=8, decimal_places=2)
    price_after = models.DecimalField(max_digits=8, decimal_places=2)
