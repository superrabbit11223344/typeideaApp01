from django.shortcuts import render
from .models import Post


def post_list(request, category_id=None, tag_id=None):
    queryset = Post.objects.all()
    if category_id:
        qeuryset = queryset.objects.filter(category_id=category_id)
    elif tag_id:
        queryset = queryset.objects.filter(tag_id=tag_id)
    context = {
        'posts': queryset
    }
    return render(request, 'blog/list.html', context=context)


def post_detail(request, post_id=None):
    context = {
        'name': 'post_detail'
    }
    return render(request, 'blog/detail.html', context=context)
