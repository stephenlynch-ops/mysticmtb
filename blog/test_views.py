from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Comment


class TestViews(TestCase):

    def test_post_list_opens_trail_list(self):
        response = self.client.get('/trails/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'trails.html')

    def test_post_detail_operates_as_expected(self):
        user = User.objects.create(username="Name")
        post = Post.objects.create(title="Test Title", author=user, status=1)
        comment = Comment.objects.create(post=post, body="Some text", name="Me", approved=True)
        self.assertEqual(comment.body, "Some text")
        self.assertEqual(post.status, 1)

    def test_open_home_page_works(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_open_cafe_page_works(self):
        response = self.client.get('/cafe/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cafe.html')
    
    def test_open_gallery_page_works(self):
        response = self.client.get('/gallery/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gallery.html')

# the remaining functions have been manually tested as part
# of the development and deployment steps.
