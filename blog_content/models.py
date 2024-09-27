from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.CharField(max_length=50)
    content = models.TextField()
    image_url = models.ImageField(upload_to='media/', blank=True, null=True, help_text="Upload an image")

    video_url = models.URLField(max_length=500, blank=True, null=True, help_text="URL of the video")
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    # New field for likes
    likes = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    poster_name = models.CharField(max_length=50)
    poster_comment = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Comment by {self.author} on {self.post.title}'

    class Meta:
        ordering = ['-created_at']

