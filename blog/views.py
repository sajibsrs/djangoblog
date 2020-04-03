from django.contrib.auth.models import User
from django.views import generic
from .models import Post


class PostList(generic.ListView):
    queryset = Post.objects.order_by('-created_on')[:10]
    template_name = 'posts/index.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'posts/detail.html'


class AuthorPosts(generic.ListView):
    model = Post

    def get_context_data(self, **kwargs):
        author_id = self.kwargs['author_id']
        author = User.objects.get(id=author_id)
        context = super().get_context_data(**kwargs)
        context['author'] = author
        context['author_posts'] = Post.objects.filter(author=author)
        return context

    template_name = 'posts/author.html'


class AuthorList(generic.ListView):
    model = User
    context_object_name = 'author_list'
    template_name = 'authors/index.html'


class AuthorDetail(generic.DetailView):
    model = User
    context_object_name = 'author'
    template_name = 'authors/detail.html'
