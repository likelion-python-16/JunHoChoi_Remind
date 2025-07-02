from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "author", "complete", "exp", "completed_at", "created_at")
    list_filter = ("complete", "author", "created_at")
    search_fields = ("name", "description", "author__username")
    ordering = ("-created_at",)
    readonly_fields = ("created_at", "updated_at", "completed_at")

    fieldsets = (
        ("기본 정보", {
            "fields": ("author", "name", "description")
        }),
        ("상태 및 경험치", {
            "fields": ("complete", "exp", "completed_at")
        }),
        ("시간 정보", {
            "fields": ("created_at", "updated_at")
        }),
    )


admin.site.register(Todo)