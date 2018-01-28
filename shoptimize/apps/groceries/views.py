from django.shortcuts import render


def discounts(request):
    return render(request, "discounts.html")

