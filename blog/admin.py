from django.contrib import admin

from .models import Author, Post, Tag


class PostInline(admin.TabularInline):
    model = Post
    extra = 1


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')
    inlines = [PostInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author_profile', 'author', 'published', 'created_at')
    list_filter = ('published', 'created_at', 'author_profile', 'tags')
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('title', 'subtitle', 'content', 'author__username')
    filter_horizontal = ('tags',)
