import pytest

from .. import models
from .fixtures import item, store


@pytest.mark.django_db
def test_create_discount(item, store):
    discount = models.GroceryDiscount.objects.create(item=item, store=store, price_before=1.00, price_after=0.95)

    assert discount.percent == 5.0
    assert discount.amount == 0.05
