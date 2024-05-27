"""Defines URL patternes for accounts."""

from django.urls import path, include

app_name = 'accounts'
urlpatterns = [
    # Includes default auth urls.
    path('', include('django.contrib.auth.urls')),
]
