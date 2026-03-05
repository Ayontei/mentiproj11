from django.contrib import admin

from .models import Sub

@admin.register(Sub)
class SubAdmin(admin.ModelAdmin):
    list_display = ["id", "subscriber", "target_user", "is_active", "created_at"]
    list_filter = ["is_active", "created_at"]
    search_fields = [
        "subscriber__username",
        "subscriber__email",
        "target_user__username",
        "target_user__email",
    ]
    list_editable = ["is_active"]
    readonly_fields = ["created_at"]
    raw_id_fields = ["subscriber", "target_user"]
    list_per_page = 50