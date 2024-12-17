from rest_framework.serializers import ModelSerializer, SerializerMethodField

from product.models import Products
from sale.models import Sales
from warehouse.models import Warehouses


class SalesSerializer(ModelSerializer):
    sale_warehouse = SerializerMethodField()
    sale_product = SerializerMethodField()

    class Meta:
        model = Sales
        fields = [
            "id",
            "total_price",
            "quantity",
            "remark",
            "slip_image",
            "is_credit",
            "is_shipped",
            "warehouse",
            "product",
        ]

    def get_sale_warehouse(self, sale):
        return Warehouses.objects.filter(pk=sale.warehouse.id).values()[0]

    def get_sale_product(self, sale):
        return Products.objects.filter(pk=sale.product.id).values()[0]
