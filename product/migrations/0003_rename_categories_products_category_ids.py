# Generated by Django 5.1.4 on 2024-12-16 07:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0002_rename_unit_products_unit_id"),
    ]

    operations = [
        migrations.RenameField(
            model_name="products",
            old_name="categories",
            new_name="category_ids",
        ),
    ]
