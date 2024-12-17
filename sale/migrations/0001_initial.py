# Generated by Django 5.1.4 on 2024-12-17 18:44

import uuid

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models

import utils.file_upload_handler


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("product", "0005_alter_products_purchase_price_and_more"),
        ("warehouse", "0003_alter_audits_unique_together_alter_audits_remark_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Sales",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("total_price", models.DecimalField(decimal_places=2, max_digits=13)),
                (
                    "quantity",
                    models.IntegerField(
                        validators=[django.core.validators.MinValueValidator(1)]
                    ),
                ),
                ("remark", models.CharField(blank=True, max_length=1024, null=True)),
                (
                    "slip_image",
                    models.ImageField(
                        max_length=1024,
                        unique=True,
                        upload_to=utils.file_upload_handler.banck_slip_upload,
                    ),
                ),
                ("is_credit", models.BooleanField(default=True)),
                ("is_shipped", models.BooleanField(default=False)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="product.products",
                    ),
                ),
                (
                    "warehouse",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="warehouse.warehouses",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
