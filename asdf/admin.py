from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "created_at")
    list_filter = ("created_at",)
    search_fields = ("title", "body")


admin.site.register(Post, PostAdmin)
