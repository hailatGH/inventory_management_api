from rest_framework.response import Response
from rest_framework.views import APIView

from user.models import Users
from user.serializers import UsersSerializer


class UsersAPIView(APIView):

    def get(self, request, *args, **kwargs):
        users = Users.objects.all()
        serializer = UsersSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        user = Users.objects.create_user(
            first_name=request.data.get("first_name"),
            last_name=request.data.get("last_name"),
            email=request.data.get("email"),
            phone_number=request.data.get("phone_number"),
            password=request.data.get("password"),
        )
        serializer = UsersSerializer(user)
        return Response(serializer.data)
