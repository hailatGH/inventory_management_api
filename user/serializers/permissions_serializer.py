from django.contrib.auth.models import Permission
from rest_framework.serializers import ModelSerializer


class PermissionsSerializer(ModelSerializer):
    class Meta:
        model = Permission
        fields = ["id", "name", "codename", "content_type"]
