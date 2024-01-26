from django.urls import path
from . import views
from .views import summarize_emails, generate_email_reply

# UrlConf
urlpatterns = [
    path('outlook/', views.get_emailpage),
    path('summarize_emails/', summarize_emails, name='summarize_emails'),
    path('generate_email_reply/', generate_email_reply, name='generate_email_reply'),
]