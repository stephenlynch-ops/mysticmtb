from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment


class TestBlogModels(TestCase):

    def test_post_str(self):
        user = User.objects.create(username="Name",)
        post = Post.objects.create(title="Test Title", author=user)
        self.assertEqual(post.title, "Test Title")


    def test_comment_str_(self):
        user = User.objects.create(username="Name",)
        post = Post.objects.create(title="Test Title", author=user)
        comment = Comment.objects.create(post=post, body="Some text", name="Me", approved=True)
        self.assertEqual(comment.body, "Some text")
        self.assertEqual(comment.name, "Me")
