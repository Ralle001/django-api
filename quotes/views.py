from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Quote
from .serializers import QuoteSerializer
import random

# List and Create Quotes
class QuoteListCreateView(generics.ListCreateAPIView):
    """
    View to list all quotes and create a new quote.
    
    Methods:
        - get: List all quotes.
        - post: Create a new quote.
    """
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer

# Retrieve, Update, Delete a Single Quote
class QuoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update, or delete a single quote.
    
    Methods:
        - get: Retrieve a single quote.
        - put: Update a single quote.
        - delete: Delete a single quote.
    """
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer

# Get Random Quote
class RandomQuoteView(APIView):
    """
    View to get a random quote.
    
    Methods:
        - get: Retrieve a random quote.
    """
    def get(self, request):
        """
        Retrieve a random quote.
        
        Args:
            request (Request): The request object.
        
        Returns:
            Response: The response containing the random quote or an error message.
        """
        quotes = Quote.objects.all()
        if not quotes.exists():
            return Response({"error": "No quotes available"}, status=status.HTTP_404_NOT_FOUND)
        random_quote = random.choice(quotes)
        serializer = QuoteSerializer(random_quote)
        return Response(serializer.data)
