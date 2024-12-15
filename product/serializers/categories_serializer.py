from rest_framework.serializers import ModelSerializer

from product.models import Categories


class CategoriesSerializer(ModelSerializer):
    class Meta:
        model = Categories
        fields = ["id", "name"]
