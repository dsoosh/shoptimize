import pytest

from shoptimize.apps.groceries import models


@pytest.fixture(scope='session')
def item():
    return models.GroceryItem.objects.create(name="Ser żółty Podlaski")


@pytest.fixture(scope='session')
def store():
    return models.GroceryStore.objects.create(name="Lidl")