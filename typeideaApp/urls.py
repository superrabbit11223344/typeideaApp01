from django.contrib import admin
from django.conf.urls import url
# from blog.views import post_list, post_detail
# from config.views import links
from blog.views import IndexView, CategoryView, TagView, PostView

from .custom_site import custom_site

urlpatterns = [
    url(r'^$', IndexView.as_view(), name="index"),
    url(r'^category/(?P<category_id>\d+)/$', CategoryView.as_view(), name='category'),
    url(r'^tag/(?P<tag_id>\d+)/$', TagView.as_view(), name='tag'),
    url(r'^post/(?P<pk>\d+)/$', PostView.as_view(), name='detail'),
    # url(r'^links/$', links),
    url(r'^admin/', admin.site.urls),
    url(r'^cus_admin/', custom_site.urls),
]
