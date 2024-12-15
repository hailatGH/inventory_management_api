from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from product.models import Products
from product.serializers import ProductsSerializer
from utils.decorators import check_permissions, paginate_response


class ProductsAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = ProductsSerializer

    @check_permissions(custom_permissions=["view_products"])
    @paginate_response()
    def get(self, request, pk=None):
        if pk:
            return get_object_or_404(Products, pk=pk)
        return Products.objects.all()

    @check_permissions(custom_permissions=["add_products"])
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @check_permissions(custom_permissions=["change_products"])
    def patch(self, request, pk):
        product = get_object_or_404(Products, pk=pk)

        serializer = self.serializer_class(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @check_permissions(custom_permissions=["delete_products"])
    def delete(self, request, pk):
        product = get_object_or_404(Products, pk=pk)
        product.delete()

        return Response(
            {"detail": "Product deleted successfully."},
            status=status.HTTP_204_NO_CONTENT,
        )
