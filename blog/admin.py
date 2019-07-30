from django.contrib import admin

from .models import Post, Category, Tag
from typeideaApp.custom_site import custom_site

@admin.register(Category, site=custom_site)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag, site=custom_site)
class TagAdmin(admin.ModelAdmin):
    pass


@admin.register(Post, site=custom_site)  # site自定义
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status', 'owner', 'created_time']
    search_fields = ['title', 'category__name', 'owner__username']
    list_filter = ['category', 'owner']
    save_on_top = True
