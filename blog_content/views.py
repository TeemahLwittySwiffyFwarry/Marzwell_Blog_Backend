from rest_framework import generics  # Import generics
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def create(self, request, *args, **kwargs):
        print("Request data:", request.data)  # Log incoming data
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'

# Handle liking a post with proper API view
@api_view(['POST'])
def like_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.likes += 1
    post.save()
    return Response({'likes': post.likes}, status=status.HTTP_200_OK)

# Handle comments for a specific post
class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post = get_object_or_404(Post, slug=self.kwargs['slug'])
        return Comment.objects.filter(post=post)

    def perform_create(self, serializer):
        post = get_object_or_404(Post, slug=self.kwargs['slug'])
        serializer.save(post=post)

# Update the URL patterns to include the comment view
