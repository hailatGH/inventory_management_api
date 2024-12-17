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
        if min_stock_level > (stock.quantity - attrs.get("quantity")):
            remaining_allowed = stock.quantity - min_stock_level
            if remaining_allowed <= 0:
                raise ValidationError(
                    {
                        "quantity": (
                            f"You cannot move that many. The maximum quantity you can move is {stock.quantity} to maintain the minimum stock level of {min_stock_level}."  # noqa E501
                            if remaining_allowed < 0
                            else f"Moving this quantity would bring the stock level below the minimum of {min_stock_level}."  # noqa E501
                        )
                    }
                )
            else:
                raise ValidationError(
                    {
                        "quantity": (
                            f"You cannot move that many. You can move at most {remaining_allowed} to maintain the minimum stock level of {min_stock_level}."  # noqa E501
                        )
                    }
                )

        stock.quantity -= attrs.get("quantity")
        stock.save()

        dest_stock = get_object_or_404(
            Stocks,
            warehouse=attrs.get("destination_warehouse"),
            product=attrs.get("product"),
        )

        dest_stock.quantity += attrs.get("quantity")
        dest_stock.save()

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
