from django.contrib.auth.models import Permission
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from user.serializers import PermissionsSerializer
from utils.decorators import paginate_response


class PermissionsAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = PermissionsSerializer

    @paginate_response()
    def get(self, request, pk=None):
        if pk:
            return get_object_or_404(Permission, pk=pk)
        else:
            return Permission.objects.all()
