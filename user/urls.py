from django.urls import path

from user.views import UsersAPIView

urlpatterns = [
    path("", UsersAPIView.as_view(), name="List users"),
]
