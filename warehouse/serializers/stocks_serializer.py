from rest_framework.serializers import ModelSerializer

from warehouse.models import Stocks


class StocksSerializer(ModelSerializer):
    class Meta:
        model = Stocks
        fields = ["id", "quantity", "warehouse", "product"]
