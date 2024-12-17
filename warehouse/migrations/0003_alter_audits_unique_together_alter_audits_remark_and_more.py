# Generated by Django 5.1.4 on 2024-12-16 05:49

import uuid

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0001_initial"),
        ("warehouse", "0002_audits_stocks"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="audits",
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name="audits",
            name="remark",
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
        migrations.CreateModel(
            name="StockMovements",
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
                (
                    "quantity",
                    models.IntegerField(
                        validators=[django.core.validators.MinValueValidator(0)]
                    ),
                ),
                ("remark", models.CharField(blank=True, max_length=1024, null=True)),
                (
                    "destination_warehouse",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="destination",
                        to="warehouse.warehouses",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="product.products",
                    ),
                ),
                (
                    "source_warehouse",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="source",
                        to="warehouse.warehouses",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
