from django.db import models

class ActiveQuerySet(models.QuerySet):
    def isactive(self):
        return self.filter(is_active=True)