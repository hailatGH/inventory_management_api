from rest_framework.serializers import ModelSerializer

from user.models import Users


class UsersSerializer(ModelSerializer):
    class Meta:
        model = Users
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "is_active",
            "date_joined",
            "groups",
            "created_at",
            "updated_at",
        ]
