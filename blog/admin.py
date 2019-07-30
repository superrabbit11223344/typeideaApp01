from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse

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
    list_display = [
        'title', 'category',
        'status', 'status_show',
        'owner', 'created_time',
        'operator'
                    ]
    # list_display_links = ['title', 'category']

    search_fields = ['title', 'category__name', 'owner__username']
    list_filter = ['category', 'owner']
    save_on_top = False

    date_hierarchy = 'created_time'
    # list_editable = ('title','status')
    # fields = (('category', 'title'), 'content')  # 布局

    fieldsets = (  # 跟fields互斥
        ('基础配置', {
            'fields': (('category', 'title'), 'content')
        }),
        ('高级配置', {
            'fields': ('tag',),
        }),
    )

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('cus_admin:blog_post_change', args=(obj.id,))
        )
    operator.short_description = '操作'


