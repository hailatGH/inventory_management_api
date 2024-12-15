from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from product.models import Categories
from product.serializers import CategoriesSerializer
from utils.decorators import check_permissions, paginate_response


class CategoriesAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = CategoriesSerializer

    @check_permissions(custom_permissions=["view_categories"])
    @paginate_response()
    def get(self, request, pk=None):
        if pk:
            return get_object_or_404(Categories, pk=pk)
        return Categories.objects.all()

    @check_permissions(custom_permissions=["add_categories"])
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @check_permissions(custom_permissions=["change_categories"])
    def patch(self, request, pk):
        category = get_object_or_404(Categories, pk=pk)

        serializer = self.serializer_class(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @check_permissions(custom_permissions=["delete_categories"])
    def delete(self, request, pk):
        category = get_object_or_404(Categories, pk=pk)
        category.delete()

        return Response(
            {"detail": "Category deleted successfully."},
            status=status.HTTP_204_NO_CONTENT,
        )
