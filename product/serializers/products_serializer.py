from decimal import Decimal

from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    ValidationError,
)

from product.models import Products


class ProductsSerializer(ModelSerializer):
    product_categories = SerializerMethodField()
    product_unit = SerializerMethodField()

    class Meta:
        model = Products
        fields = [
            "id",
            "name",
            "purchase_price",
            "retail_price",
            "sale_percentage",
            "min_stock_level",
            "created_at",
            "updated_at",
            "product_unit",
            "product_categories",
            "unit",
            "categories",
        ]

    def validate(self, attrs):
        one = Decimal(1)
        hundred = Decimal(100)

        retail_price = Decimal(attrs.get("retail_price"))
        purchase_price = Decimal(attrs.get("purchase_price"))
        sale_percentage = one + (Decimal(attrs.get("sale_percentage")) / hundred)

        min_retail_price = sale_percentage * purchase_price
        if retail_price < min_retail_price:
            raise ValidationError(
                {
                    "retail_price": (
                        f"The retail price must be at least " f"({min_retail_price})."
                    )
                }
            )

        return super().validate(attrs)

    def get_product_categories(self, product):
        return product.categories.all().values()

    def get_product_unit(self, product):
        if product.unit:
            return {
                "id": product.unit.id,
                "name": product.unit.name,
                "created_at": product.unit.created_at,
                "updated_at": product.unit.updated_at,
            }
        return None
