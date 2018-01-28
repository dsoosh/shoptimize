import pytest
from django.urls import reverse

from .. import views


def test_list_all_discounts_when_no_discounts_available(client):
    response = client.get(reverse('discounts'))
    assert response.status_code == 200
