from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from blog_home.models import Post


class PostList(ListView):
    template_name = 'index.html'
    post: Post = Post()

    def get_queryset(self):
        return Post.objects.filter(status=1).order_by('-created_on')


class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'
