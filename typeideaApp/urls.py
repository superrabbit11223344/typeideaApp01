from django.contrib import admin
from django.conf.urls import url
# from blog.views import post_list, post_detail
from config.views import LinkListView
from blog.views import IndexView, CategoryView, TagView, PostDetailView, SearchView, AuthorView

from .custom_site import custom_site

urlpatterns = [
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^category/(?P<category_id>\d+)/$', CategoryView.as_view(), name="category-list"),
    url(r'^tag/(?P<tag_id>\d+)/$', TagView.as_view(), name="tag-list"),
    url(r'^post/(?P<post_id>\d+).html/$', PostDetailView.as_view(), name="post-detail"),
    url(r'^links/$', LinkListView.as_view(), name="links"),
    url(r'^search/$', SearchView.as_view(), name='search'),
    url(r'^author/(?P<owner_id>\d+)/$', AuthorView.as_view(), name='author'),
    url(r'^admin/', admin.site.urls),
    url(r'^cus_admin/', custom_site.urls),
]
