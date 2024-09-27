from django.contrib import admin
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('title','slug', 'content','video_url', 'created_at', 'image_url', 'author', 'likes')
    
    # Fields to be editable in the admin form
    fields = ('title', 'slug', 'content','video_url', 'image_url', 'author', 'created_at', 'likes')
    
    # Optional: Add a method to display a thumbnail of the image in the list view
    def thumbnail(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="100" height="100"/>'
        return 'No image'
    
    # Specify that the thumbnail method should be rendered as HTML
    thumbnail.allow_tags = True

    # Optional: Add filter options or search functionality
    list_filter = ('created_at',)
    search_fields = ('title', 'content')

admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('post','poster_name', 'poster_comment', 'created_at',)
    
    # Fields to be editable in the admin form
    fields = ('post','poster_name', 'poster_comment', 'created_at')
    
    

    # Optional: Add filter options or search functionality
    list_filter = ('created_at',)
    search_fields = ('title', 'content')

admin.site.register(Comment, CommentAdmin)
