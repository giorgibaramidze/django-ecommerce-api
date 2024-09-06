from django.db import models
from django.core import checks
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.signals import post_delete
from django.dispatch import receiver
import logging

logger = logging.getLogger(__name__)

class OrderField(models.PositiveIntegerField):
    def __init__(self, unique_for_field=None, *args, **kwargs):
        self.unique_for_field = unique_for_field
        super().__init__(*args, **kwargs)

    def check(self, **kwargs):
        # Return any errors from super() checks along with our own check
        return [*super().check(**kwargs), *self._check_for_field_attribute(**kwargs)]

    def _check_for_field_attribute(self, **kwargs):
        if self.unique_for_field is None:
            return [
                checks.Error(
                    "'unique_for_field' is required for OrderField.",
                    obj=self,
                    id='fields.E001',
                )
            ]
        elif self.unique_for_field not in [f.name for f in self.model._meta.get_fields()]:
            return [
                checks.Error(
                    f"'{self.unique_for_field}' is not a valid field name in the model.",
                    obj=self,
                    id='fields.E002',
                )
            ]
        return []

    def pre_save(self, model_instance, add):
        if getattr(model_instance, self.attname) is None:
            try:
                # Get the queryset filtered by the related field (e.g. product)
                qs = self.model.objects.filter(**{self.unique_for_field: getattr(model_instance, self.unique_for_field)})
                last_item = qs.latest(self.attname)
                value = last_item.order + 1
            except ObjectDoesNotExist:
                # If no previous item exists, start at 1
                value = 1
            except Exception as e:
                logger.error(f"Unexpected error while determining 'order' for {model_instance}: {e}")
                raise e
            return value
        return super().pre_save(model_instance, add)

    class Meta:
        # Indexing for performance when filtering by unique_for_field and order
        indexes = [
            models.Index(fields=['product', 'order']),
        ]