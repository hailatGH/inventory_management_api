from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from sale.models import Sales
from sale.serializers import SalesSerializer
from utils.decorators import check_permissions, paginate_response


class SalesAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = SalesSerializer

    @check_permissions(custom_permissions=["view_sales"])
    @paginate_response()
    def get(self, request, pk=None):
        if pk:
            return get_object_or_404(Sales, pk=pk)
        return Sales.objects.all()

    @check_permissions(custom_permissions=["add_sales"])
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @check_permissions(custom_permissions=["change_sales"])
    def patch(self, request, pk):
        sale = get_object_or_404(Sales, pk=pk)

        serializer = self.serializer_class(sale, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
