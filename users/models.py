from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ADMIN = 'admin'
    SUPERVISOR = 'supervisor'
    DATA_ENTRY = 'data_entry'
    
    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (SUPERVISOR, 'Supervisor'),
        (DATA_ENTRY, 'Data Entry'),
    ]
    
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=DATA_ENTRY)
