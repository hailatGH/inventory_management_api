from django.urls import path

from user.views import UsersAPIView

urlpatterns = [
    path("users/", UsersAPIView.as_view(), name="List/Create users APIView"),
    path(
        "users/<uuid:pk>/",
        UsersAPIView.as_view(),
        name="Get,Update,Delete user APIView",
    ),
]

urlpatterns = [
    path(
        "users/",
        UsersAPIView.as_view(),
        name="user-create-list",
    ),
    path(
        "users/<uuid:pk>/",
        UsersAPIView.as_view(),
        name="user-detail-patch-delete",
    ),
]
