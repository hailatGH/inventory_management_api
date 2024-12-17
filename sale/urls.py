from django.urls import path

from sale.views import SalesAPIView

urlpatterns = [
    path("sales/", SalesAPIView.as_view(), name="sale-create-list"),
    path("sales/<uuid:pk>/", SalesAPIView.as_view(), name="sale-detail-patch"),
]
