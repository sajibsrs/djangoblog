from django.views import generic
from .models import Post


class PostList(generic.ListView):
    queryset = Post.objects.order_by('-created_on')[:10]
    template_name = 'posts/index.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'posts/detail.html'
