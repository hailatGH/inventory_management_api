from rest_framework.serializers import ModelSerializer

from product.models import Products


class ProductsSerializer(ModelSerializer):
    class Meta:
        model = Products
        fields = [
            "id",
            "name",
            "purchase_price",
            "retail_price",
            "sale_percentage",
            "min_stock_level",
            "unit",
            "categories",
        ]
