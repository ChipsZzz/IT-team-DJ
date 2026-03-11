from django.db import models
from django.contrib.auth.models import User


class Item(models.Model):

    CATEGORY_CHOICES = [
        ("books", "Books"),
        ("electronics", "Electronics"),
        ("fashion", "Fashion"),
        ("other", "Other")
    ]

    STATUS_CHOICES = [
        ("available", "Available"),
        ("sold", "Sold")
    ]

    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="items"
    )

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    title = models.CharField(max_length=200)

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    description = models.TextField()

    image = models.ImageField(
        upload_to="items/",
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="available"
    )

    favourites = models.ManyToManyField(
        User,
        related_name="favourite_items",
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title