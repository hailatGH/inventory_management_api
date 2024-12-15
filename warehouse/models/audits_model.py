import uuid

from django.core.validators import MinValueValidator
from django.db import models

from product.models import Products
from utils.models import Timestamps
from warehouse.models import Warehouses


class Audits(Timestamps):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    stock_quantity = models.IntegerField(null=False, validators=[MinValueValidator(0)])
    counted_quantity = models.IntegerField(
        null=False, validators=[MinValueValidator(0)]
    )
    warehouse = models.ForeignKey(Warehouses, on_delete=models.CASCADE, null=False)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, null=False)
    remark = models.CharField(max_length=1024, null=True)

    class Meta:
        unique_together = ("product", "warehouse")
