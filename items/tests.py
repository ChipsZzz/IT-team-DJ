from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from .models import Item, Category
from comments.models import Comment


class ItemCommentTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser",
            password="12345"
        )

        self.category = Category.objects.create(
            name="Electronics"
        )

        self.item = Item.objects.create(
            owner=self.user,
            category=self.category,
            title="Test Item",
            description="Test description",
            price=10
        )

    def test_item_creation(self):
        self.assertEqual(self.item.title, "Test Item")
        self.assertEqual(self.item.owner.username, "testuser")
        self.assertEqual(self.item.category.name, "Electronics")

    def test_comment_creation(self):
        comment = Comment.objects.create(
            item=self.item,
            author=self.user,
            text="Nice item"
        )
        self.assertEqual(comment.text, "Nice item")
        self.assertEqual(comment.item, self.item)

    def test_item_has_comment(self):
        Comment.objects.create(
            item=self.item,
            author=self.user,
            text="Great"
        )
        self.assertEqual(self.item.comments.count(), 1)

    def test_item_detail_view_status_code(self):
        response = self.client.get(reverse("item_detail", args=[self.item.id]))
        self.assertEqual(response.status_code, 200)

    def test_logged_in_user_can_post_comment(self):
        self.client.login(username="testuser", password="12345")
        response = self.client.post(
            reverse("item_detail", args=[self.item.id]),
            {"text": "Posted from test"}
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.item.comments.count(), 1)