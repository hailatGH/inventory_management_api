from rest_framework.serializers import ModelSerializer

from warehouse.models import Warehouses


class WarehousesSerializer(ModelSerializer):
    class Meta:
        model = Warehouses
        fields = ["id", "name", "location"]
