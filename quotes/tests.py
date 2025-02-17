from rest_framework.test import APITestCase
from rest_framework import status
from quotes.models import Quote

class QuoteAPITestCase(APITestCase):
    """
    Test case for the Quote API.
    
    Methods:
        - setUp: Set up test data.
        - test_list_quotes: Test listing all quotes.
        - test_random_quote: Test retrieving a random quote.
        - test_create_quote: Test creating a new quote.
        - test_retrieve_quote: Test retrieving a specific quote.
        - test_update_quote: Test updating a quote.
        - test_delete_quote: Test deleting a quote.
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

    def test_create_quote(self):
        """
        Test creating a new quote.
        """
        data = {'text': 'New test quote', 'author': 'New Author'}
        response = self.client.post('/api/quotes/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Quote.objects.count(), 3)
        self.assertEqual(Quote.objects.get(id=response.data['id']).text, 'New test quote')

    def test_retrieve_quote(self):
        """
        Test retrieving a specific quote.
        """
        response = self.client.get(f'/api/quotes/{self.quote1.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['text'], self.quote1.text)

    def test_update_quote(self):
        """
        Test updating a quote.
        """
        data = {'text': 'Updated test quote', 'author': 'Updated Author'}
        response = self.client.put(f'/api/quotes/{self.quote1.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.quote1.refresh_from_db()
        self.assertEqual(self.quote1.text, 'Updated test quote')

    def test_delete_quote(self):
        """
        Test deleting a quote.
        """
        response = self.client.delete(f'/api/quotes/{self.quote1.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Quote.objects.count(), 1)
