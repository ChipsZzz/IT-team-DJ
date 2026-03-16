from django.test import TestCase
from django.contrib.auth.models import User
from items.models import Item
from .models import Comment


class CommentTest(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(
            username="commenter",
            password="password123"
        )

        self.item = Item.objects.create(
            owner=self.user,
            title="Test Item",
            price=10,
            description="Test description",
            category="books"
        )


    def test_comment_creation(self):

        comment = Comment.objects.create(
            item=self.item,
            author=self.user,
            text="Nice item!"
        )

        self.assertEqual(comment.text, "Nice item!")
        self.assertEqual(comment.author.username, "commenter")


    def test_comment_relationships(self):

        comment = Comment.objects.create(
            item=self.item,
            author=self.user,
            text="Great!"
        )

        self.assertEqual(comment.item.title, "Test Item")
        self.assertEqual(comment.author.username, "commenter")


    def test_comment_string_representation(self):

        comment = Comment.objects.create(
            item=self.item,
            author=self.user,
            text="Nice!"
        )

        expected = f"Comment by {self.user.username} on item {self.item.id}"

        self.assertEqual(str(comment), expected)


    def test_comment_ordering(self):

        Comment.objects.create(
            item=self.item,
            author=self.user,
            text="First comment"
        )

        Comment.objects.create(
            item=self.item,
            author=self.user,
            text="Second comment"
        )

        comments = Comment.objects.all()

        self.assertEqual(comments.first().text, "Second comment")