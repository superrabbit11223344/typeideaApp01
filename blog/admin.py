from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse

from .models import Post, Category, Tag
from typeideaApp.custom_site import custom_site
from typeideaApp.custom_admin import BaseOwnerAdmin

from .adminforms import PostAdminForm

# from xadmin.layout import Row, Fieldset
# from xadmin.filters import manager
# from xadmin.filters import RelatedFieldListFilter

# import xadmin

# class CategoryOwnerFilter(RelatedFieldListFilter):
#
#     @classmethod
#     def test(cls, field, request, params, model, admin_view, field_path):
#         return field.name == 'category'
#
#     def __init__(self, field, request, params, model, model_admin, field_path):
#         super().__init__(field, request, params, model, model_admin, field_path)
#         # 重新获取lookup_choices,根据owner过滤
#         self.lookup_choices = Category.objects.filter(owner=request.user).values_list('id', 'name')
#
#
# manager.register(CategoryOwnerFilter, take_priority=True)


@admin.register(Post, site=custom_site)  # site自定义
class PostAdmin(BaseOwnerAdmin):
    form = PostAdminForm
    list_display = [
        'title', 'category',
        'status', 'status_show',
        'owner', 'created_time',
        'operator', 'pv', 'uv',
                    ]
    # list_display_links = ['title', 'category']
    list_display_links = []

    list_filter = ['category', 'owner']
    search_fields = ['title', 'category__name']
    save_on_top = True
    actions_on_top = True

    date_hierarchy = 'created_time'



    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('admin:blog_post_change', args=(obj.id,))
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






