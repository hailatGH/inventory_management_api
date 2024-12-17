import uuid

from django.core.validators import MinValueValidator
from django.db import models

from product.models import Products
from utils.models import Timestamps
from warehouse.models.warehouses_model import Warehouses


class StockMovements(Timestamps):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    quantity = models.IntegerField(null=False, validators=[MinValueValidator(0)])
    source_warehouse = models.ForeignKey(
        Warehouses, on_delete=models.CASCADE, null=False, related_name="source"
    )
    destination_warehouse = models.ForeignKey(
        Warehouses, on_delete=models.CASCADE, null=False, related_name="destination"
    )
    product = models.ForeignKey(Products, on_delete=models.CASCADE, null=False)
    remark = models.CharField(max_length=1024, null=True, blank=True)
