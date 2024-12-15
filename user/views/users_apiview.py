from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from user.models import Users
from user.serializers import UsersSerializer
from utils.decorators import paginate_response


class UsersAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = UsersSerializer

    @paginate_response()
    def get(self, request, pk=None):
        if pk:
            return get_object_or_404(Users, pk=pk)
        else:
            return Users.objects.all()

    def post(self, request):
        password = request.data.get("password")
        if not password:
            raise ValidationError({"password": "Password is required."})

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(password)
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        user = get_object_or_404(Users, pk=pk)
        password = request.data.get("password")

        serializer = self.serializer_class(user, data=request.data, partial=True)
        if serializer.is_valid():
            if password:
                user.set_password(password)
                user.save()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = get_object_or_404(Users, pk=pk)
        user.delete()
        return Response(
            {"detail": "User deleted successfully."}, status=status.HTTP_204_NO_CONTENT
        )
