from django.contrib import admin
from .models import Post, Blogger, Comment

# Register your models here.
admin.site.register(Post)
admin.site.register(Blogger)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'created_at', 'active')
    list_filter = ('active', 'created_at')
    search_fields = ('name', 'body')
    actions = ["approve_comments"]

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

