import pytest

from claims.models import Claim
from claims.services import create_claim


@pytest.mark.django_db
def test_create_claim():
    data = {
        'title': 'ПК',
        'description': 'Компьютер производителя "Asus"',
        'type': 'Computers'
    }
    create_claim(data)
    assert Claim.objects.filter(**data).exists()