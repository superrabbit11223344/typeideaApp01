from django.views.generic import View, ListView, DetailView  # ListView 更适合做列表展示
from django.views.generic.detail import SingleObjectMixin
from django.http import HttpResponse
from django.shortcuts import render

from .models import Post, Tag, Category
from config.models import SideBar
from comment.models import Comment


def post_list(request, category_id=None, tag_id=None):
    tag = None
    category = None

    if tag_id:
        try:
            tag = Tag.objects.get(id=tag_id)
        except Tag.DoesNotExist:
            post_list = []
        else:
            post_list = tag.post_set.filter(status=Post.STATUS_NORMAL)
    else:
        post_list = Post.objects.filter(status=Post.STATUS_NORMAL)
        if category_id:
            post_list = post_list.filter(category_id=category_id)
    context = {
        'category': category,
        'tag': tag,
        'post_list': post_list,
        'sidebars': SideBar.get_all(),
    }
    context.update(Category.get_navs())
    return render(request, 'blog/list.html', context=context)


def post_detail(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        post = None

    context = {
        'post': post,
    }
    context.update(Category.get_navs())
    return render(request, 'blog/detail.html', context=context)