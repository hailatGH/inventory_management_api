from datetime import datetime


def banck_slip_upload(instance, filename):
    return f"BankSlips/{instance.warehouse.name}/{instance.product.name}/{instance.pk}/{str(datetime.now())}_{instance.product.name}_{filename}"  # noqa E501
