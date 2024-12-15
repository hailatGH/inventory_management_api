import uuid

from django.db import models

from utils.models import Timestamps


class Warehouses(Timestamps):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150, unique=True)
    location = models.CharField(max_length=1024, null=False)
