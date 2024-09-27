from rest_framework import serializers
from .models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'  # or specify fields as needed

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)  # Adjust according to your model

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'likes', 'comments', 'slug', 'author', 'video_url', 'image_url','created_at']  # Include 'comments' here
        
    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image_url:
            return request.build_absolute_uri(obj.image_url.url)
        return None
