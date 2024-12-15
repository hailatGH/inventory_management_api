from rest_framework.serializers import ModelSerializer

from product.models import Units


class UnitsSerializer(ModelSerializer):
    class Meta:
        model = Units
        fields = ["id", "name"]
