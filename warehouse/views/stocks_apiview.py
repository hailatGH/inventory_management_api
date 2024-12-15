from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from utils.decorators import check_permissions, paginate_response
from warehouse.models import Stocks, Warehouses
from warehouse.serializers import StocksSerializer


class StocksAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = StocksSerializer

    @check_permissions(custom_permissions=["view_stocks"])
    @paginate_response()
    def get(self, request, warehouse_id=None, pk=None):
        if pk:
            return get_object_or_404(Stocks, pk=pk)
        else:
            warehouse = get_object_or_404(Warehouses, pk=warehouse_id)
            return Stocks.objects.filter(warehouse=warehouse)

    @check_permissions(custom_permissions=["change_stocks"])
    def patch(self, request, pk):
        quantity = request.data.get("quantity", None)
        if not quantity:
            raise ValidationError({"quantity": "Quantity is required."})

        stock = get_object_or_404(Stocks, pk=pk)

        serializer = self.serializer_class(stock, data=request.data, partial=True)
        if serializer.is_valid():
            stock.quantity = quantity
            stock.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
