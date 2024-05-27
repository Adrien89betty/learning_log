"""Defines URL patternes for accounts."""

from django.urls import path, include
from . import views

app_name = 'accounts'
urlpatterns = [
    # Includes default auth urls.
    path('', include('django.contrib.auth.urls')),
    # Registration page.
    path('register/', views.register, name='register'),
]
