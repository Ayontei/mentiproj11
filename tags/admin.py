from django.contrib import admin

from .models import Tags

@admin.register(Tags)
class TagAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "slug", "created_at"]
    list_filter = ["created_at"]
    search_fields = ["name", "slug"]
    prepopulated_fields = {"slug": ("name",)}  # автоматическое заполнение slug из name