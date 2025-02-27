from django import forms
from .models import *
from inventory.models import *

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description', 'quantity', 'expiration_date', 'supplier']