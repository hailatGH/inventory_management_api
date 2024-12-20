from django.urls import path

from warehouse.views import (
    AuditsAPIView,
    StockMovementsAPIView,
    StocksAPIView,
    WarehousesAPIView,
)

urlpatterns = [
    path("warehouses/", WarehousesAPIView.as_view(), name="warehouse-create-list"),
    path(
        "warehouses/<uuid:pk>/",
        WarehousesAPIView.as_view(),
        name="warehouse-detail-patch-delete",
    ),
    path(
        "warehouse/<uuid:warehouse_id>/stocks/",
        StocksAPIView.as_view(),
        name="warehouse-stock-list",
    ),
    path(
        "stocks/<uuid:pk>/",
        StocksAPIView.as_view(),
        name="stock-detail-patch",
    ),
    path(
        "audits/",
        AuditsAPIView.as_view(),
        name="audit-create-list",
    ),
    path(
        "audits/<uuid:pk>/",
        AuditsAPIView.as_view(),
        name="audit-detail",
    ),
    path(
        "stock_movements/",
        StockMovementsAPIView.as_view(),
        name="stock-movement-create-list",
    ),
    path(
        "stock_movements/<uuid:pk>/",
        StockMovementsAPIView.as_view(),
        name="stock-movement-detail",
    ),
]
