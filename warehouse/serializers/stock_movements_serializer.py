from django.shortcuts import get_object_or_404
from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    ValidationError,
)

from product.models import Products
from warehouse.models import StockMovements, Stocks, Warehouses


class StockMovementsSerializer(ModelSerializer):
    stock_product = SerializerMethodField()
    stock_source_warehouse = SerializerMethodField()
    stock_destination_warehouse = SerializerMethodField()

    class Meta:
        model = StockMovements
        fields = [
            "id",
            "quantity",
            "remark",
            "stock_product",
            "stock_source_warehouse",
            "stock_destination_warehouse",
            "source_warehouse",
            "destination_warehouse",
            "product",
        ]

    def validate(self, attrs):
        stock = get_object_or_404(
            Stocks,
            warehouse=attrs.get("source_warehouse"),
            product=attrs.get("product"),
        )
        stock.quantity < attrs.get("quantity")
        min_stock_level = stock.product.min_stock_level
        if min_stock_level >= (stock.quantity - attrs.get("quantity")):
            raise ValidationError(
                {
                    "min_stock_level": (
                        f"The allowed quantity to move must be at most "
                        f"({stock.quantity - min_stock_level})."
                    )
                }
            )

        stock.quantity -= attrs.get("quantity")
        stock.save()

        return super().validate(attrs)

    def get_stock_product(self, stock_movement):
        return Products.objects.filter(pk=stock_movement.product.id).values()[0]

    def get_stock_source_warehouse(self, stock_movement):
        return Warehouses.objects.filter(
            pk=stock_movement.source_warehouse.id
        ).values()[0]

    def get_stock_destination_warehouse(self, stock_movement):
        return Warehouses.objects.filter(
            pk=stock_movement.destination_warehouse.id
        ).values()[0]
