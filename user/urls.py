from django.urls import path

from user.views import GroupsAPIView, PermissionsAPIView, UsersAPIView

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
    path(
        "groups/",
        GroupsAPIView.as_view(),
        name="group-create-list",
    ),
    path(
        "groups/<uuid:pk>/",
        GroupsAPIView.as_view(),
        name="group-detail-patch-delete",
    ),
    path(
        "permissions/",
        PermissionsAPIView.as_view(),
        name="permission-list",
    ),
]
