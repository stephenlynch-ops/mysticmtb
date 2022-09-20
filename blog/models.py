from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, 'Draft'), (1, 'Published'))

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    map = CloudinaryField('map', default='placeholder_map')
    image_one = CloudinaryField('image_one', default='placeholder_one')
    image_two = CloudinaryField('image_two', default='placeholder_two')
    difficulty = models.CharField(max_length=10)
    time = models.CharField(max_length=10)
    distance = models.CharField(max_length=10)
    ave_speed = models.CharField(max_length=20)
    up = models.CharField(max_length=10)
    down = models.CharField(max_length=10)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    published_on = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    

class Meta:
    ordering = ['-created_on']


def __str__(self):
    return self.title


def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']
    
    def __str__(self):
        return f"Comment {self.body} made by {self.name}"


