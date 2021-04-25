from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import BlogPost
# Create your views here.

class BlogPostListView(ListView):
    model = BlogPost
    template_name = "blog/blog_list.html"
    context_object_name = 'blog_post_list'
    


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = "blog/blog_detail.html"
    context_object_name = "post"