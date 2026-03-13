from django.test import TestCase
from django.contrib.auth.models import User
from .models import Address


class AddressModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username="user1")

    def test_create_address(self):
        address = Address.objects.create(
            user=self.user,
            city="Glasgow",
            postcode="G12",
            address_line="University Avenue"
        )

        self.assertEqual(address.city, "Glasgow")
        self.assertEqual(address.user.username, "user1")