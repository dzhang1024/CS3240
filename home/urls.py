from django.urls import path
from django.views.generic.base import TemplateView
from . import views
from django.urls import path, include
from django.views.generic import TemplateView

app_name = "home"
urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('profile/update/', views.update_profile, name='update_profile'),
    # path('profile/update/', views.UpdateProfileView.as_view(), name='update_profile'),
    path('issues/', views.IssueList.as_view(), name='issues'),
    path('issues/<int:pk>/', views.IssueDetail.as_view(), name='issues_detail'),
    path('issues/<int:pk>/email_page', views.contact, name='email_page'),
    path('issues/<int:pk>/email_page/success/', views.success, name='success'), #successurl
    path('issues/submit/', views.SubmitIssue.as_view(), name='submit_issue'),
]
