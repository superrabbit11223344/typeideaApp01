from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50, verbose_name="标题")
    desc = models.CharField(max_length=255, blank=True, verbose_name="摘要")
    category = models.ForeignKey(Category, verbose_name="分类")




class Category(models.Model):
    pass