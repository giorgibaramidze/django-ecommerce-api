from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import ProductLine
import logging

logger = logging.getLogger(__name__)

@receiver(post_delete, sender=ProductLine)
def reorder_product_lines(sender, instance, **kwargs):
    """
    Signal to reorder product lines after a ProductLine is deleted.
    """
    try:
        qs = sender.objects.filter(product=instance.product).order_by('order')
        for i, obj in enumerate(qs, start=1):
            obj.order = i
            obj.save()
    except Exception as e:
        logger.error(f"Error while reordering product lines after deletion: {e}")
