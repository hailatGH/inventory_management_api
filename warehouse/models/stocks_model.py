import uuid

from django.core.validators import MinValueValidator
from django.db import models

from product.models import Products
from utils.models import Timestamps
from warehouse.models import Warehouses


class Stocks(Timestamps):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    quantity = models.IntegerField(null=False, validators=[MinValueValidator(0)])
    warehouse = models.ForeignKey(Warehouses, on_delete=models.CASCADE, null=False)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, null=False)

    class Meta:
        unique_together = ("product", "warehouse")
