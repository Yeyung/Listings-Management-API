from django.test import TestCase
from rest_framework.test import APIClient
from .models import Shop, Listing

class ListingTests(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.shop = Shop.objects.create(name="Test Shop", description="Test Description")
        self.listing = Listing.objects.create(shop=self.shop, title="Test Listing", description="Test Description", price=100)

    def test_create_listing(self):
        response = self.client.post(f'/api/shops/{self.shop.id}/listings/', {'title': 'New Listing', 'description': 'New Description', 'price': 200})
        self.assertEqual(response.status_code, 201)

    def test_get_listing(self):
        response = self.client.get(f'/api/listings/{self.listing.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['title'], 'Test Listing')

