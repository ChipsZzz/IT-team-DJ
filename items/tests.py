from django.test import TestCase
from django.contrib.auth.models import User
from .models import Item


class ItemModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username="testuser")

    def test_item_creation(self):
        item = Item.objects.create(
            title="Test Item",
            description="Test description",
            price=10,
            owner=self.user
        )

        self.assertEqual(item.title, "Test Item")
        self.assertEqual(item.owner.username, "testuser")
        self.assertEqual(item.price, 10)