from rest_framework.serializers import ModelSerializer

from warehouse.models import Audits


class AuditsSerializer(ModelSerializer):
    class Meta:
        model = Audits
        fields = [
            "id",
            "stock_quantity",
            "counted_quantity",
            "warehouse",
            "product",
            "remark",
        ]
