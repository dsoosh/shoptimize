from django.db import models


class GroceryItem(models.Model):
    name = models.CharField(max_length=32)


class GroceryStore(models.Model):
    name = models.CharField(max_length=32, unique=True)
