from django.urls import path
from django.views.generic.base import TemplateView
from . import views
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

app_name = "home"
urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('profile/update/', views.update_profile, name='update_profile'),
    # path('profile/update/', views.UpdateProfileView.as_view(), name='update_profile'),
    path('issues/', views.IssueList.as_view(), name='issues'),
    path('issues/<int:pk>/', views.IssueDetail.as_view(), name='issues_detail'),
    path('issues/<int:pk>/saved', views.save_issue, name='save_issue'),
    path('issues/<int:pk>/email_page', views.contact, name='email_page'),
    path('issues/<int:pk>/email_page/success/', views.success, name='success'), #successurl
    path('issues/submit/', login_required(views.SubmitIssue.as_view()), name='submit_issue'),
]

# Derived from
# https://simpleisbetterthancomplex.com/tutorial/2016/08/01/how-to-upload-files-with-django.html
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
