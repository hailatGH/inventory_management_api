from django.urls import path

from warehouse.views import WarehousesAPIView

urlpatterns = [
    path("warehouses/", WarehousesAPIView.as_view(), name="warehouse-create-list"),
    path(
        "warehouses/<uuid:pk>/",
        WarehousesAPIView.as_view(),
        name="warehouse-detail-patch-delete",
    ),
]
