from django.test import TestCase
from django.contrib.auth.models import User
from .models import Item


class ItemModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="password123"
        )

    def test_item_creation(self):
        item = Item.objects.create(
            owner=self.user,
            title="Test Item",
            price=10.00,
            description="Test description",
            category="books"
        )

        self.assertEqual(item.title, "Test Item")
        self.assertEqual(item.owner.username, "testuser")

    def test_item_string_representation(self):
        item = Item.objects.create(
            owner=self.user,
            title="Laptop",
            price=500,
            description="Gaming laptop",
            category="electronics"
        )

        self.assertEqual(str(item), "Laptop")


class ItemViewTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="viewer",
            password="password123"
        )

        self.item = Item.objects.create(
            owner=self.user,
            title="Phone",
            price=200,
            description="Smartphone",
            category="phones"
        )

    def test_item_list_page(self):
        response = self.client.get("/items/")
        self.assertEqual(response.status_code, 200)

    def test_item_detail_page(self):
        response = self.client.get(f"/items/{self.item.id}/")
        self.assertEqual(response.status_code, 200)

    def test_item_create_requires_login(self):
        response = self.client.get("/items/create/")
        self.assertNotEqual(response.status_code, 200)