from django.urls import path
from django.views.generic.base import TemplateView
from . import views
from django.urls import path, include
from django.views.generic import TemplateView

app_name = "home"
urlpatterns = [
    path('', views.home, name='home'),
    path('issues', views.issues, name='issues'),
]
