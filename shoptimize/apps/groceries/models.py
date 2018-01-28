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
    percent = models.DecimalField(max_digits=5, decimal_places=2)
    amount = models.DecimalField(max_digits=8, decimal_places=2)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.percent = round(1 - self.price_after / self.price_before, 2) * 100
        self.amount = round(self.price_before - self.price_after, 2)
        super(GroceryDiscount, self).save()
