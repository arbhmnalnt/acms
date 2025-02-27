from django.db import models
from django.contrib.auth.models import AbstractUser
from core.models import BaseModel

class Report(BaseModel):
    report_type = models.CharField(max_length=100)
    generated_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()