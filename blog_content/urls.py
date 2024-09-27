from django.urls import path
from .views import PostListCreateView, PostRetrieveUpdateDestroyView, like_post, CommentListCreateView

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<slug:slug>/', PostRetrieveUpdateDestroyView.as_view(), name='post-detail'),
    path('posts/<slug:slug>/like/', like_post, name='post-like'),
    path('posts/<slug:slug>/comments/', CommentListCreateView.as_view(), name='post-comments'),
]
