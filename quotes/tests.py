from rest_framework.test import APITestCase
from rest_framework import status
from .models import Quote

class QuoteAPITestCase(APITestCase):
    """
    Test case for the Quote API.
    
    Methods:
        - setUp: Set up test data.
        - test_list_quotes: Test listing all quotes.
        - test_random_quote: Test retrieving a random quote.
    """
    def setUp(self):
        """
        Set up test data.
        """
        self.quote1 = Quote.objects.create(text="Test quote 1", author="Author 1")
        self.quote2 = Quote.objects.create(text="Test quote 2", author="Author 2")

    def test_list_quotes(self):
        """
        Test listing all quotes.
        """
        response = self.client.get('/api/quotes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_random_quote(self):
        """
        Test retrieving a random quote.
        """
        response = self.client.get('/api/quotes/random/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
