import uuid

from django.core.validators import MinValueValidator
from django.db import models

from product.models import Products
from utils.file_upload_handler import banck_slip_upload
from utils.models import Timestamps
from warehouse.models import Warehouses


class Sales(Timestamps):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    warehouse = models.ForeignKey(
        Warehouses, on_delete=models.DO_NOTHING, null=False, blank=False
    )
    product = models.ForeignKey(
        Products, on_delete=models.DO_NOTHING, null=False, blank=False
    )
    total_price = models.DecimalField(max_digits=13, decimal_places=2, null=False)
    quantity = models.IntegerField(null=False, validators=[MinValueValidator(1)])
    remark = models.CharField(max_length=1024, null=True, blank=True)
    slip_image = models.ImageField(
        upload_to=banck_slip_upload, max_length=1024, null=True, blank=True
    )
    is_credit = models.BooleanField(default=True)
    is_shipped = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.product.name}"
