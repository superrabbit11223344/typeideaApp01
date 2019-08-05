from django.contrib import admin


from typeideaApp.custom_site import custom_site
from .models import Comment
from typeideaApp.custom_admin import BaseOwnerAdmin


@admin.register(Comment, site=custom_site)
class CommentAdmin(BaseOwnerAdmin):
    list_display = [
        'post', 'content', 'nickname',
        'website', 'email', 'status',
        'created_time',
    ]
    list_filter = ['post__title']
    search_fields = ['content', 'nickname']
    date_hierarchy = 'created_time'
    fields = (
        ('post', 'content', 'nickname'),
        ('website', 'email'),
    )