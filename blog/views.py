from django.shortcuts import render
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage

from .models import Post, Tag, Category
from config.models import SideBar
from comment.models import Comment


def post_list(request, category_id=None, tag_id=None):
    page = request.GET.get('page', 1)  # 获取page的第一个参数，即总页数
    page_size = 4  # 每页的个数
    try:
        page = int(page)
    except TypeError:
        page = 1

    queryset = Post.objects.all()   # 获取所有的Post对象
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
    paginator = Paginator(queryset, page_size)  # 分页器，第一个参数是需要展示的对象queryset，第二个参数是每一页展示的数据个数
    try:
        posts = paginator.page(page)   # paginator的page方法，对page进行分页处理
    except EmptyPage:   # 异常捕获
        posts = paginator.page(paginator.num_pages)

    categories = Category.objects.filter(status=1)  # TODO: fix magic number
    nav_cates = []
    cates = []
    for cate in categories:
        if cate.is_nav:
            nav_cates.append(cate)
        else:
            cates.append(cate)

    side_bars = SideBar.objects.filter(status=1)
    recently_posts = Post.objects.filter(status=1)[:10]
    # hot_posts = Post.objects.filter(status=1).order_by('views')[:10]
    recently_comments = Comment.objects.filter(status=1)[:10]


    context = {
        'posts': posts,
        'nav_cates': nav_cates,
        'cates': cates,
        'side_bars': side_bars,
        'recently_posts': recently_posts,
        'recently_comments': recently_comments,
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
