def banck_slip_upload(instance, filename):
    return f"BankSlips/{instance.warehouse.name}/{instance.product.name}/{instance.pk}/{filename}"
