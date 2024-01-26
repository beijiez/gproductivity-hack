from django.urls import path
from . import views
from .views import summarize_emails

# UrlConf
urlpatterns = [
    path('outlook/', views.get_emailpage),
    path('summarize_emails/', summarize_emails, name='summarize_emails')
]