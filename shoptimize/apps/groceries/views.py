from django.shortcuts import render

from . import models


def discounts(request):
    discounts = models.GroceryDiscount.objects.all()
    return render(request, template_name='discounts.html', context={'discounts': discounts})
