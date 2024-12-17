import uuid

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from product.models.categories_model import Categories
from product.models.units_model import Units
from utils.models import Timestamps


class Products(Timestamps):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150, unique=True)
    purchase_price = models.DecimalField(max_digits=13, decimal_places=2, null=False)
    retail_price = models.DecimalField(max_digits=13, decimal_places=2, null=False)
    sale_percentage = models.IntegerField(
        null=False, validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    min_stock_level = models.IntegerField(null=False, validators=[MinValueValidator(0)])
    unit = models.ForeignKey(Units, on_delete=models.DO_NOTHING)
    categories = models.ManyToManyField(Categories)
