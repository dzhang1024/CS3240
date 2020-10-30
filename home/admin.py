from django.contrib import admin

# Register your models here.
from .models import Issue, Email

admin.site.register(Issue)
admin.site.register(Email)