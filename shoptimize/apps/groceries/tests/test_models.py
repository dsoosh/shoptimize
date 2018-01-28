import datetime
import pytest
from django.core.exceptions import ValidationError

from .. import models
from .fixtures import item, store

today = datetime.datetime.today()
one_day = datetime.timedelta(days=1)
yesterday = today - one_day
tomorrow = today + one_day


@pytest.mark.django_db
def test_create_discount(item, store):
    discount = models.GroceryDiscount.objects.create(item=item, store=store, price_before=1.00, price_after=0.95)

    assert discount.percent == 5.0
    assert discount.amount == 0.05


@pytest.mark.django_db
def test_price_before_must_be_higher_than_after_discount(item, store):
    with pytest.raises(ValidationError):
        models.GroceryDiscount.objects.create(item=item, store=store, price_before=1.00, price_after=1.05)


@pytest.mark.django_db
def test_cant_create_a_discount_that_is_already_expired(item, store):
    with pytest.raises(ValidationError):
        models.GroceryDiscount.objects.create(item=item,
                                              store=store,
                                              price_before=1.00,
                                              price_after=0.99,
                                              begins=tomorrow,
                                              ends=today)


@pytest.mark.django_db
def test_cant_create_a_discount_that_ends_before_it_begins(item, store):
    with pytest.raises(ValidationError):
        models.GroceryDiscount.objects.create(item=item,
                                              store=store,
                                              price_before=1.00,
                                              price_after=0.99,
                                              begins=today,
                                              ends=yesterday)
