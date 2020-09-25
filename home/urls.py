from django.urls import path
from django.views.generic.base import TemplateView
from . import views
from django.urls import path, include
from django.contrib import admin
from django.views.generic import TemplateView

app_name = "home"
urlpatterns = [
    path('', TemplateView.as_view(template_name="base.html")),
    # path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
]
