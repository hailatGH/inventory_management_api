# Generated by Django 5.1.4 on 2024-12-17 19:57

from django.db import migrations, models

import utils.file_upload_handler


class Migration(migrations.Migration):

    dependencies = [
        ("sale", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sales",
            name="slip_image",
            field=models.ImageField(
                max_length=1024, upload_to=utils.file_upload_handler.banck_slip_upload
            ),
        ),
    ]
