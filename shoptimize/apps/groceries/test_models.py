import pytest

from . import models


@pytest.mark.django_db
def test_create_grocery_item():
    item = models.GroceryItem.objects.create(name="Ser żółty Podlaski")
    assert item.name == "Ser żółty Podlaski"


@pytest.mark.django_db
def test_create_grocery_store():
    store = models.GroceryStore.objects.create(name="Lidl")
    assert store.name == "Lidl"
