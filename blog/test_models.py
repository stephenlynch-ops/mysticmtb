""" Imports TestCase from django.test"""
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment


class TestBlogModels(TestCase):
    """ Inherits TestCase for all functions below
    """

    def test_post_str(self):
        """ Tests a post can be created and title is returned.
        """
        user = User.objects.create(username="Name",)
        post = Post.objects.create(title="Test Title", author=user)
        self.assertEqual(post.title, "Test Title")

    def test_comment_str_(self):
        """ Tests a comment can be created and that the body and
            author can be returned.
        """
        user = User.objects.create(username="Name",)
        post = Post.objects.create(title="Test Title", author=user)
        comment = Comment.objects.\
            create(post=post, body="Some text", name="Me", approved=True)
        self.assertEqual(comment.body, "Some text")
        self.assertEqual(comment.name, "Me")
