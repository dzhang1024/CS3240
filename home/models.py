from django.db import models

# Create your models here.
class Issues(models.Models)
    issue_name = models.CharField(max_length=100)
    description = models.TextField()