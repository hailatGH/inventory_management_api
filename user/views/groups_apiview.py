from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from user.serializers import GroupsSerializer
from utils.decorators import check_permissions, paginate_response


class GroupsAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = GroupsSerializer

    @check_permissions(custom_permissions=["view_group"])
    @paginate_response()
    def get(self, request, pk=None):
        if pk:
            return get_object_or_404(Group, pk=pk)
        else:
            return Group.objects.all()

    @check_permissions(custom_permissions=["add_group"])
    def post(self, request):
        name = request.data.get("name")
        if not name:
            raise ValidationError({"name": "Name is required."})

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            group = serializer.save()
            group.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @check_permissions(custom_permissions=["change_group"])
    def patch(self, request, pk):
        group = get_object_or_404(Group, pk=pk)

        serializer = self.serializer_class(group, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @check_permissions(custom_permissions=["delete_group"])
    def delete(self, request, pk):
        group = get_object_or_404(Group, pk=pk)
        group.delete()

        return Response(
            {"detail": "Group deleted successfully."}, status=status.HTTP_204_NO_CONTENT
        )
