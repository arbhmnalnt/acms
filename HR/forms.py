from django import forms
from .models import *
from inventory.models import *

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['user', 'position', 'salary', 'hire_date']

