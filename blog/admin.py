""" imports admin from django.contrib"""
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """Sets the admin fields in Django admin page for posts.
    """
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'published_on', 'author')
    list_display = ('title', 'slug', 'status', 'published_on', 'difficulty')
    search_fields = ('title', 'difficulty', 'content')
    summernote_fields = ('content')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """Sets the admin fields in Django admin page for comments.
    """
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email_address', 'body', 'approved')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        """Modifies commetn approved status from False to True
        """
        queryset.update(approved=True)
