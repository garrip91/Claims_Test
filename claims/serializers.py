from rest_framework import serializers

from claims.models import Claim


class ClaimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Claim
        fields = '__all__'