import pytest

from claims.models import Claim


@pytest.mark.django_db
def test_create_claim_view(api_client):
    data = {
        'title': 'ПК',
        'description': 'Компьютер производителя "Asus"',
        'type': 'Computers'
    }
    response = api_client.post(path='/api/claim/create', format='json', data=data)

    assert response.status_code == 201
    assert Claim.objects.filter(**data).exists()