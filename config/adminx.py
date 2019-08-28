from django.contrib import admin

from typeideaApp.custom_site import custom_site
from .models import Link, SideBar
from typeideaApp.custom_admin import BaseOwnerAdmin

import xadmin

@xadmin.sites.register(Link)
class LinkAdmin(BaseOwnerAdmin):
    list_display = [
        'title', 'href', 'status',
        'weight', 'owner', 'created_time',
    ]
    date_hierarchy = 'created_time'
    fields = (
        ('title', 'href', 'status', 'weight'),
    )


@xadmin.sites.register(SideBar)
class SideBarAdmin(BaseOwnerAdmin):
    list_display = [
        'title', 'display_type', 'content',
        'status', 'owner', 'created_time',
    ]
    date_hierarchy = 'created_time'
    fields = (
        'title', 'display_type', 'status', 'content', 'owner'
    )