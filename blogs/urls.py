from django.conf.urls import url

from blogs.views import BlogList, Blog, Post

urlpatterns = [
    url(r'^$', BlogList.as_view(), name="blog_list"),
    url(r'^(?P<pk>\d+)/$', Blog.as_view(), name="blog"),
    url(r'^(?P<blog>\d+)/post/(?P<pk>\d+)/$', Post.as_view(), name="post"),
]