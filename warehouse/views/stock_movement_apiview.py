from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from utils.decorators import check_permissions, paginate_response
from warehouse.models import StockMovements
from warehouse.serializers import StockMovementsSerializer


class StockMovementsAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = StockMovementsSerializer

    @check_permissions(custom_permissions=["view_stockmovements"])
    @paginate_response()
    def get(self, request, warehouse_id=None, pk=None):
        if pk:
            return get_object_or_404(StockMovements, pk=pk)
        return StockMovements.objects.all()

    @check_permissions(custom_permissions=["add_stockmovements"])
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
