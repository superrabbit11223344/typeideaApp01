from django.db import models

# Create your models here.

class Post(models.Model):
    STATUS_ITEMS = (
        (1, '上线'),
        (2, '草稿'),
        (3, '删除'),
    )
    title = models.CharField(max_length=50, verbose_name="标题")
    desc = models.CharField(max_length=255, blank=True, verbose_name="摘要")
    category = models.ForeignKey('Category', verbose_name="分类", on_delete=True)
    tag = models.ManyToManyField('Tag', verbose_name="标签")

    content = models.TextField(verbose_name="内容", help_text="注：目前只支持markdown数据")
    status = models.IntegerField(default=1, choices=,verbose_name="状态")






class Category(models.Model):
    pass