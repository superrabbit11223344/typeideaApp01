from django.contrib import admin

from typeideaApp.custom_site import custom_site
from .models import Link, SideBar
from typeideaApp.custom_admin import BaseOwnerAdmin


@admin.register(Link, site=custom_site)
class LinkAdmin(BaseOwnerAdmin):
    list_display = [
        'title', 'href', 'status',
        'weight', 'owner', 'created_time',
    ]
    date_hierarchy = 'created_time'
    fields = (
        ('title', 'href', 'status', 'weight'),
    )


@admin.register(SideBar, site=custom_site)
class SideBarAdmin(BaseOwnerAdmin):
    list_display = [
        'title', 'display_type', 'content',
        'status', 'owner', 'created_time',
    ]
    date_hierarchy = 'created_time'
    fields = (
        'title', 'display_type', 'status', 'content', 'owner'
    )