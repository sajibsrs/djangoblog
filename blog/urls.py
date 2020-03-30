from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='posts-index'),
    path('posts/<int:pk>', views.PostDetail.as_view(), name='posts-detail'),
    path('authors/<int:author_id>/posts', views.AuthorPosts.as_view(), name='author-posts'),
    path('authors/<int:pk>', views.Authors.as_view(), name='authors')
]