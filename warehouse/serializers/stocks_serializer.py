from rest_framework.serializers import ModelSerializer

from product.serializers import ProductsSerializer
from warehouse.models import Stocks
from warehouse.serializers.warehouses_serializer import WarehousesSerializer


class StocksSerializer(ModelSerializer):
    warehouse = WarehousesSerializer(read_only=True)
    product = ProductsSerializer(read_only=True)

    class Meta:
        model = Stocks
        fields = "__all__"
