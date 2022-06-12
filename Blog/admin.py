from django.contrib import admin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'slug', 'author', 'created', 'publish')
    list_filter = ('status', 'author', 'publish')
    search_fields = ('title', 'text')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('status', 'publish')
    date_hierarchy = 'publish'
    raw_id_fields = ('author',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'post', 'active', 'created', 'updated')
    ordering = ('active',)
    raw_id_fields = ('post',)
    list_filter = ('created', 'updated', 'active')
    list_search = ('text', 'email', 'name')