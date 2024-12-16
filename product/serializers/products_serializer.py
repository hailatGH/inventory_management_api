from rest_framework.serializers import ModelSerializer

from product.models import Products
from product.serializers.categories_serializer import CategoriesSerializer
from product.serializers.units_serializer import UnitsSerializer


class ProductsSerializer(ModelSerializer):
    categories = CategoriesSerializer(many=True, read_only=True)
    unit = UnitsSerializer(read_only=True)

    class Meta:
        model = Products
        fields = "__all__"
