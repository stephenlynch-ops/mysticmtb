""" Imports django shortcuts """
from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404, reverse, HttpResponse
from django.views import generic, View
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
import pytz
from .models import Post, Comment
from .forms import CommentForm


class PostList(generic.ListView):
    """ Uses post model
        Checks for published posts, sorts by date
        loads trails.html template
        paginates articles by 3 (per page)
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-published_on')
    template_name = 'trails.html'
    paginate_by = 3


class PostDetail(View):
    """ Inherits View for the loading of the trail articles
    """

    def get(self, request, slug, *args, **kwargs):
        """ Set parameters receiving post detail
            Checks posted comments are approved before render
            Checks likes for user liked
            Returns trail_detail.html template
        """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True, user_removed=0).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "trail_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """ Set parameters posting comments detail
            Checks posted comments are approved before render
            Checks likes for user liked
            Returns trail_detail.html template

            Tests comment form is valid and user is authorised to post
            prior to posting.
        """
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True, user_removed=0).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "trail_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm(),
            },
        )


class PostLike(View):
    """ Inherits View for the below functions
    """

    def post(self, request, slug):
        """ Checks user is on list of likes and allows toggle of
            like button.
        """
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


def open_home_page(request):
    """ Collects current hour
        compares to opening / closing time and returns message
        based on if conditions.
        Opens index.html template.
    """

    opening_time = 8
    closing_time = 19

    tz_London = pytz.timezone('Europe/London')
    datetime_London = datetime.now(tz_London)
    now = int(datetime_London.strftime("%H"))

    if (now >= closing_time and now < 24):
        hours = ((24 - now) + opening_time)
        context = {
            'message': f"There are {hours} until the trails open tomorrow"
            }
    elif now < opening_time:
        hours = (opening_time - now)
        context = {
            'message': f"There are {hours} until the trails open today"
            }
    else:
        context = {
            'message': "The trails are OPEN"
            }

    return render(request, 'index.html', context)


def open_cafe_page(request):
    """ Opens cafe.html template
    """

    return render(request, 'cafe.html')


def open_gallery_page(request):
    """ Opens gallery.html template
    """
    return render(request, 'gallery.html')

class DeleteComment(View):

    def delete_comment(self, request, slug, *args, **kwargs):

        our_comment = get_object_or_404(Comment, pk=comment_id)
        current_score = our_comment.user_removed
        new_score = current_score =+ 1

        return new_score