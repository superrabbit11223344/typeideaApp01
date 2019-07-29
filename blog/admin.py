from django.contrib import admin

from .models import Post, Category, Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Post)  # site自定义
class PostAdmin(admin.ModelAdmin):
    pass
