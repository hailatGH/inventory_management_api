from django.urls import path

from product.views import CategoriesAPIView, ProductsAPIView, UnitsAPIView

urlpatterns = [
    path("categories/", CategoriesAPIView.as_view(), name="category-create-list"),
    path(
        "categories/<uuid:pk>/",
        CategoriesAPIView.as_view(),
        name="category-detail-patch-delete",
    ),
    path("units/", UnitsAPIView.as_view(), name="unit-create-list"),
    path(
        "units/<uuid:pk>/",
        UnitsAPIView.as_view(),
        name="unit-detail-patch-delete",
    ),
    path("products/", ProductsAPIView.as_view(), name="product-create-list"),
    path(
        "products/<uuid:pk>/",
        ProductsAPIView.as_view(),
        name="product-detail-patch-delete",
    ),
]
