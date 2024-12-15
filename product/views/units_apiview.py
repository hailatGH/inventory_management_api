from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from product.models import Units
from product.serializers import UnitsSerializer
from utils.decorators import check_permissions, paginate_response


class UnitsAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = UnitsSerializer

    @check_permissions(custom_permissions=["view_units"])
    @paginate_response()
    def get(self, request, pk=None):
        if pk:
            return get_object_or_404(Units, pk=pk)
        return Units.objects.all()

    @check_permissions(custom_permissions=["add_units"])
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @check_permissions(custom_permissions=["change_units"])
    def patch(self, request, pk):
        unit = get_object_or_404(Units, pk=pk)

        serializer = self.serializer_class(unit, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @check_permissions(custom_permissions=["delete_units"])
    def delete(self, request, pk):
        unit = get_object_or_404(Units, pk=pk)
        unit.delete()

        return Response(
            {"detail": "Unit deleted successfully."},
            status=status.HTTP_204_NO_CONTENT,
        )
