from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from blogs.models import Blog, Post
from comments.models import Comment
from core.models import User


class HomePageView(TemplateView):
    template_name = "core/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['users_count'] = User.objects.all().count()
        context['blogs_count'] = Blog.objects.all().count()
        context['posts_count'] = Post.objects.all().count()
        context['comments_count'] = Comment.objects.all().count()
        return context