from claims.models import Claim


def create_claim(data):
    Claim.objects.create(**data)