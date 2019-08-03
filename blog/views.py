from django.shortcuts import render
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage

from .models import Post, Tag


def post_list(request, category_id=None, tag_id=None):
    queryset = Post.objects.all()
    page = request.GET.get('page', 1)
    page_size = 4
    try:
        page = int(page)
    except TypeError:
        page = 1

    if category_id:
        # 分类页面
        queryset = queryset.filter(category_id=category_id)
    elif tag_id:
        # 标签页面
        try:
            tag = Tag.objects.get(id=tag_id)
        except Tag.DoesNotExist:
            queryset = []
        else:
            queryset = tag.post_set.all()
    paginator = Paginator(queryset, page_size)
    try:
        posts = paginator.page(page)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        'posts': posts,
    }
    return render(request, 'blog/list.html', context=context)


def post_detail(request, post_id=None):
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        raise Http404('出错啦！！文章找不到')
    context = {
        'post': post
    }
    return render(request, 'blog/detail.html', context=context)
