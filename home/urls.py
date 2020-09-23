from django.urls import path
from django.views.generic.base import TemplateView
from . import views

app_name = "home"
urlpatterns = [
    path('', views.home, name='home'),
]