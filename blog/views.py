from django.shortcuts import render
from django.views import generic
from .models import Post


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-published_on')
    template_name = 'trails.html'
    paginate_by = 6


def open_home_page(request):
    return render(request, 'index.html')

