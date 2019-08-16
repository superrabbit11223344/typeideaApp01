from django.contrib import admin
from django.conf.urls import url
from blog.views import post_list, post_detail
from config.views import links
# from blog.views import IndexView, CategoryView, TagView, PostView

from .custom_site import custom_site

urlpatterns = [
    url(r'^$', post_list, name="index"),
    url(r'^category/(?P<category_id>\d+)/$', post_list, name="category-list"),
    url(r'^tag/(?P<tag_id>\d+)/$', post_list, name="tag-list"),
    url(r'^post/(?P<post_id>\d+).html/$', post_detail, name="post-detail"),
    url(r'^links/$', links, name="links"),
    url(r'^admin/', admin.site.urls),
    url(r'^cus_admin/', custom_site.urls),
]
