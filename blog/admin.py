from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment



@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'published_on', 'author')
    list_display = ('title', 'slug', 'status', 'published_on', 'difficulty')
    search_fields = ('title', 'difficulty', 'content')
    summernote_fields = ('content')


class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email_address', 'body', 'approved')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
