import uuid

from django.db import models

from utils.models import Timestamps


class Units(Timestamps):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=150, unique=True)
