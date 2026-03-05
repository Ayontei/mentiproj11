from django.contrib import admin

from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    search_fields = ['title', 'content', 'author__username']
    list_filter = ['is_published', 'categories', 'tags', 'author']
    list_display = ['id', 'title', 'author', 'is_published', 'created_at']
    filter_horizontal = ['tags']  # Удобный виджет для ManyToManyField