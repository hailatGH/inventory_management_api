# Generated by Django 5.1.4 on 2024-12-16 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="products",
            old_name="unit",
            new_name="unit_id",
        ),
    ]