from django.db import models
from django.contrib.auth.models import AbstractUser
from core.models import BaseModel

class Item(BaseModel):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    quantity = models.PositiveIntegerField()
    expiration_date = models.DateField(blank=True, null=True)
    supplier = models.CharField(max_length=200, blank=True, null=True)

class StockTransaction(BaseModel):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity_change = models.IntegerField()
    transaction_type = models.CharField(max_length=10, choices=[('add', 'Addition'), ('remove', 'Removal')])
    transaction_date = models.DateTimeField(auto_now_add=True)
