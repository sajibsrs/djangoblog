from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='posts.index'),
    path('posts/<int:pk>', views.PostDetail.as_view(), name='posts.detail'),
]