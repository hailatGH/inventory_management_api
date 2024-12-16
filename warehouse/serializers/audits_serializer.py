from rest_framework.serializers import ModelSerializer

from product.serializers import ProductsSerializer
from warehouse.models import Audits
from warehouse.serializers.warehouses_serializer import WarehousesSerializer


class AuditsSerializer(ModelSerializer):
    warehouse = WarehousesSerializer(read_only=True)
    product = ProductsSerializer(read_only=True)

    class Meta:
        model = Audits
        fields = "__all__"
