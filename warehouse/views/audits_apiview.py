from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from utils.decorators import check_permissions, paginate_response
from warehouse.models import Audits
from warehouse.serializers import AuditsSerializer


class AuditsAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = AuditsSerializer

    @check_permissions(custom_permissions=["view_audits"])
    @paginate_response()
    def get(self, request, pk=None):
        if pk:
            return get_object_or_404(Audits, pk=pk)
        else:
            return Audits.objects.all()

    @check_permissions(custom_permissions=["add_audits"])
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
