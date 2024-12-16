from django.db.models.signals import post_save
from django.dispatch import receiver

from product.models import Products
from warehouse.models import Stocks, Warehouses


@receiver(post_save, sender=Products)
def create_stock_entries(sender, instance, created, **kwargs):
    if created:
        for warehouse in Warehouses.objects.all():
            Stocks.objects.create(
                warehouse=warehouse,
                product=instance,
                quantity=0,  # Or any default quantity you prefer
            )
