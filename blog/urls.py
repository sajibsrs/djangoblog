from . import views
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='index'),
    path('<int:pk>/', views.PostDetail.as_view(), name='detail'),
]