from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from utils.decorators import check_permissions, paginate_response
from warehouse.models import Warehouses
from warehouse.serializers import WarehousesSerializer


class WarehousesAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = WarehousesSerializer

    @check_permissions(custom_permissions=["view_warehouses"])
    @paginate_response()
    def get(self, request, pk=None):
        if pk:
            return get_object_or_404(Warehouses, pk=pk)
        else:
            return Warehouses.objects.all()

    @check_permissions(custom_permissions=["add_warehouses"])
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @check_permissions(custom_permissions=["change_warehouses"])
    def patch(self, request, pk):
        warehouse = get_object_or_404(Warehouses, pk=pk)

        serializer = self.serializer_class(warehouse, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @check_permissions(custom_permissions=["delete_warehouses"])
    def delete(self, request, pk):
        warehouse = get_object_or_404(Warehouses, pk=pk)
        warehouse.delete()

        return Response(
            {"detail": "Warehouse deleted successfully."},
            status=status.HTTP_204_NO_CONTENT,
        )
