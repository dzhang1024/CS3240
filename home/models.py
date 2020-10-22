from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify

# Create your models here.
class Issue(models.Model):
    issue_name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=100)
    slug = models.SlugField(default='', editable=False, max_length=200, null = False)

    def __str__(self):
        self.slug = slugify(issue_name, allow_unicode=True)
        return self.issue_name