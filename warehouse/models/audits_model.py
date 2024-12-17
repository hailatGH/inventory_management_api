import uuid

from django.core.validators import MinValueValidator
from django.db import models

from product.models import Products
from utils.models import Timestamps
from warehouse.models.stocks_model import Stocks
from warehouse.models.warehouses_model import Warehouses


class Audits(Timestamps):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    stock_quantity = models.IntegerField(null=False, validators=[MinValueValidator(0)])
    counted_quantity = models.IntegerField(
        null=False, validators=[MinValueValidator(0)]
    )
    warehouse = models.ForeignKey(Warehouses, on_delete=models.CASCADE, null=False)
    product = models.ForeignKey(Products, on_delete=models.CASCADE, null=False)
    remark = models.CharField(max_length=1024, null=True, blank=True)

    def save(self, *args, **kwargs):
        stock = Stocks.objects.filter(
            warehouse=self.warehouse, product=self.product
        ).first()
        if stock:
            self.stock_quantity = stock.quantity
        super().save(*args, **kwargs)
