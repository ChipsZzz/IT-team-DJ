from django.contrib.auth.models import User
from django.db import models


class Address(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )

    city = models.CharField(max_length=100)

    postcode = models.CharField(max_length=20)

    address_line = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username