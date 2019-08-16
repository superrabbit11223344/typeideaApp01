from django.views.generic import View, ListView, DetailView     # ListView 更适合做列表展示
from django.views.generic.detail import SingleObjectMixin

from .models import Post, Tag, Category
from config.models import SideBar
from comment.models import Comment



class CommonMixin():
    def get_category_context(self):
        categories = Category.objects.filter(status=1)  # TODO: fix magic number
        nav_cates = []
        cates = []
        for cate in categories:
            if cate.is_nav:
                nav_cates.append(cate)
            else:
                cates.append(cate)
        return {
            'nav_cates': nav_cates,
            'cates': cates
        }

    def get_context_data(self, **kwargs):
        # context = super(CommonMixin, self).get_context_data()
        context = super().get_context_data(**kwargs)

        side_bars = SideBar.objects.filter(status=1)
        recently_posts = Post.objects.filter(status=1)[:10]
        # hot_posts = Post.objects.filter(status=1).order_by('views')[:10]
        recently_comments = Comment.objects.filter(status=1)[:10]

        context.update({
            'side_bars': side_bars,
            'recently_posts': recently_posts,
            'recently_comments': recently_comments,
            'footer_name': 'power by superrabbit'
        })
        context.update(self.get_category_context())
        # return super(CommonMixin, self).get_context_data(**kwargs)
        return context


class BasePostsView(ListView, CommonMixin):
    model = Post
    template_name = 'themes/default/template/blog/list.html'
    context_object_name = 'posts'
    paginate_by = 3
    allow_empty = True


class IndexView(BasePostsView):
    pass


class CategoryView(BasePostsView):
    def get_queryset(self):
        qs = super(CategoryView, self).get_queryset()
        cate_id = self.kwargs.get('category_id')
        qs = qs.filter(category_id=cate_id)
        return qs


class TagView(BasePostsView):
    def get_queryset(self):
        tag_id = self.kwargs.get('tag_id')
        try:
            tag = Tag.objects.get(id=tag_id)
        except Tag.DoesNotExist:
            return []

        posts = tag.posts.all()
        return posts


class PostView(DetailView, CommonMixin):
    model = Post
    template_name = 'themes/default/template/blog/detail.html'
    context_object_name = 'post'



