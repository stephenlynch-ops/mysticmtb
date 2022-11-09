""" imports models from django.db"""
import uuid
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, 'Draft'), (1, 'Published'))
USER_REMOVED = ((0, 'No'), (1, 'Yes'))


class Post(models.Model):
    """ Post model fields:-
        Slug = Slug field
        Map, image one and image two = Cloudinary field
        Content = Text field
        Author = User, on delete to Cascade removal
        Published on = Date, time field
        Likes = many to many field
        Status = Integer field
        All others are Char Fields.
    """
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
    author = models.\
        ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    published_on = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)
    status = models.IntegerField(choices=STATUS, default=0)


class Meta:
    """ Ordering of posts set to -created on date / time
    """
    ordering = ['-created_on']


def __str__(self):
    """ Returns post title
    """
    return self.title


def number_of_likes(self):
    """ Returns count of likes
    """
    return self.likes.count()


class Comment(models.Model):
    """ Sets fields for Comment
        Post = Foreignkey
        Name = Char field
        Email = Email field
        body = Text field
        Created on = date, time field
        Approved = Boolean field
        Years riding = Char field.
    """
    post = models.\
        ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    years_riding = models.CharField(max_length=2, default=0)
    user_removed = models.IntegerField(choices=USER_REMOVED, default=0)

    class Meta:
        """ Ordering of comments set to -created on date / time
        """
        ordering = ['created_on']

    def __str__(self):
        """ Returns f string
        """
        return f"Comment {self.body} made by {self.name}"

