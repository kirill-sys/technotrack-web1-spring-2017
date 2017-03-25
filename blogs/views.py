# -- coding: utf-8 --
from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView, ListView

from blogs.models import Blog, Post


class BlogList(ListView):
    template_name = "blogs/blog_list.html"
    model = Blog


class Blog(DetailView):
    template_name = 'blogs/blog.html'
    model = Blog


class Post(DetailView):
    template_name = 'blogs/post.html'
    model = Post
