from django.urls import path
from .views import QuoteListCreateView, QuoteDetailView, RandomQuoteView

urlpatterns = [
    path('quotes/', QuoteListCreateView.as_view(), name='quote-list-create'),
    path('quotes/<int:pk>/', QuoteDetailView.as_view(), name='quote-detail'),
    path('quotes/random/', RandomQuoteView.as_view(), name='random-quote'),
]

"""
URL configuration for the quotes app.

The `urlpatterns` list routes URLs to views.

Routes:
    - 'quotes/': List and create quotes.
    - 'quotes/<int:pk>/': Retrieve, update, and delete a single quote.
    - 'quotes/random/': Retrieve a random quote.
"""
