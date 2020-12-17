from django.conf.urls import url
from django.views.generic import ListView, DetailView
from .models import Post

urlpatterns = [
    url('^$', ListView.as_view(
        queryset=Post.objects.all().order_by("-data"),
        template_name="lista_post.html", paginate_by=5), name="lista"),
    
    url('^asd/(?P<id>\d+)/(?P<slug>[\w-]+)/$', DetailView.as_view(
        model=Post,
        template_name="post_singular.html"), name="singular"),
]
