from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse

from .models import Post, Category, Tag
from typeideaApp.custom_site import custom_site
from typeideaApp.custom_admin import BaseOwnerAdmin
from .adminforms import PostAdminForm

@admin.register(Post, site=custom_site)  # site自定义
class PostAdmin(BaseOwnerAdmin):
    form = PostAdminForm
    list_display = [
        'title', 'category',
        'status', 'status_show',
        'owner', 'created_time',
        'operator'
                    ]
    # list_display_links = ['title', 'category']
    list_display_links = []

    list_filter = ['category', 'owner']
    search_fields = ['title', 'category__name']
    save_on_top = True
    actions_on_top = True

    date_hierarchy = 'created_time'
    # list_editable = ('title','status')
    # fields = (('category', 'title'), 'content')  # 布局

    # fieldsets = (  # 跟fields互斥
    #     ('基础配置', {
    #         'fields': (
    #             ('category', 'title'),
    #             'desc',
    #             'status',
    #             'content'
    #         )
    #     }),
    #     ('高级配置', {
    #         'fields': ('tag',),
    #     }),
    # )
    fields = (
        ('category', 'title'),
        'desc',
        'status',
         'content',
        'tag',
            )

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('cus_admin:blog_post_change', args=(obj.id,))
        )
    operator.short_description = '操作'


@admin.register(Category, site=custom_site)
class CategoryAdmin(BaseOwnerAdmin):
    list_display = ['name', 'status', 'is_nav', 'created_time']
    fields = (
        'name', 'status',
        'is_nav',
    )


@admin.register(Tag, site=custom_site)
class TagAdmin(BaseOwnerAdmin):
    list_display = ['name', 'status', 'created_time']
    fields = (
        'name', 'status'
    )






