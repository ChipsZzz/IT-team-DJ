from django.test import TestCase
from django.contrib.auth.models import User
from items.models import Item
from .models import CartItem


class CartTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="cartuser",
            password="password123"
        )

        self.item = Item.objects.create(
            owner=self.user,
            title="Bike",
            price=100,
            description="Mountain bike",
            category="bikes"
        )

    def test_add_to_cart(self):
        CartItem.objects.create(
            user=self.user,
            item=self.item
        )

        cart_items = CartItem.objects.filter(user=self.user)

        self.assertEqual(cart_items.count(), 1)

    def test_cart_item_user_relationship(self):
        cart_item = CartItem.objects.create(
            user=self.user,
            item=self.item
        )

        self.assertEqual(cart_item.user.username, "cartuser")