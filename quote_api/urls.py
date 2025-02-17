from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('quotes.urls')),
]

"""
URL configuration for the quote_api project.

The `urlpatterns` list routes URLs to views.

Routes:
    - 'admin/': Admin site.
    - 'api/': Include URLs from the quotes app.
"""
