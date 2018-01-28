import pytest
from django.urls import reverse

from .. import models
from .fixtures import item, store


@pytest.mark.django_db
def test_list_all_discounts_when_no_discounts_available(client):
    response = client.get(reverse('discounts'))
    assert response.status_code == 200
    assert len(response.context['discounts']) == 0


@pytest.mark.django_db
def test_list_all_discounts_when_some_discounts_are_available(client, item, store):
    discount = models.GroceryDiscount.objects.create(item=item, store=store, price_before=2.00, price_after=1.00)
    response = client.get(reverse('discounts'))
    assert response.status_code == 200
    assert len(response.context['discounts']) == 1
    assert response.context['discounts'][0] == discount
