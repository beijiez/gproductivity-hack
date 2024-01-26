from django.urls import path
from . import views

# UrlConf
urlpatterns = [
    path('', views.home),
]