from django.test import TestCase
from django.contrib.auth.models import User
from .models import Item, Category


class ItemModelTest(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            username="testuser",
            password="12345"
        )

        self.category = Category.objects.create(
            name="Electronics"
        )

    def test_create_item(self):

        item = Item.objects.create(
            title="Test Item",
            price=100,
            owner=self.user,
            category=self.category
        )

        self.assertEqual(item.title, "Test Item")


    def test_item_string(self):

        item = Item.objects.create(
            title="Phone",
            price=50,
            owner=self.user,
            category=self.category
        )

        self.assertEqual(str(item), item.title)