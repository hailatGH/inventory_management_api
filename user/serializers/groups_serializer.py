from django.contrib.auth.models import Group
from rest_framework.serializers import ModelSerializer


class GroupsSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ["name", "permissions"]
