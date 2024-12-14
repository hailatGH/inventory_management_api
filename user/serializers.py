from rest_framework.serializers import ModelSerializer

from user.models import Users


class UsersSerializer(ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"
