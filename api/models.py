from django.db import models
from datetime import datetime   
from django.utils import timezone

# Create your models here.
class Movie(models.Model):
    Name = models.CharField(max_length=100)
    Descriptions = models.TextField()
    Date_Of_Release = models.DateField(default=timezone.now(), blank=True)

    def __str__(self):
        return self.Name