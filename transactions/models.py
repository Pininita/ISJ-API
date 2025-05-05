from django.db import models

from .choices import TRANSACTION_TYPE_CHOICES
from django.conf import settings

# Create your models here.

class Transaction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='transactions', blank=True, null=True)
    description = models.CharField(max_length=400)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    city = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPE_CHOICES) # se cambia el nombre por unos mas adecuado, type es una palabra reserbada de django
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_transaction_type_display()} - {self.amount} ({self.city})"