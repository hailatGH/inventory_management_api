# Generated by Django 5.1.4 on 2024-12-17 19:59

from django.db import migrations, models

import utils.file_upload_handler


class Migration(migrations.Migration):

    dependencies = [
        ("sale", "0002_alter_sales_slip_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sales",
            name="slip_image",
            field=models.ImageField(
                blank=True,
                max_length=1024,
                null=True,
                upload_to=utils.file_upload_handler.banck_slip_upload,
            ),
        ),
    ]