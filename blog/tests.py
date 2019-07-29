from django.contrib.auth.models import User
from django.db import connection
from django.test import TestCase
from django.db.models import Count

from .models import Category


class TestCategory(TestCase):
    def setUp(self):
        self.user = user = User.objects.create_user('the5fire', 'fake@email.com', 'password')
        # for i in range(10):
        #     category_name = 'cate_%s' % i
        #     Category.objects.create(name=category_name, owner=user)
        Category.objects.bulk_create([     # 批量创建
            Category(name='bate__bulk_%s' % i, owner=user)
            for i in range(10)
        ])


    def test_filter(self):
        queryset = Category.objects.all()
        print(queryset)
        categories = queryset.filter(status=1)
        print(categories)
        print('-------')
        categories = queryset.exclude(status=0)
        print(categories)
        categories = queryset.order_by('id')
        # categories = queryset.first()
        print(categories)
        categories = Category.objects.get(id=1)
        print(categories)
        categories = Category.objects.get_or_create(name='django', owner=self.user)
        print(categories)
        print('-----------------')
        category = Category.objects.filter(status=1)
        print(category)
        result = category.update(name="update_1")
        print(result)

        categories = Category.objects.filter(status=1).defer('created_time')
        for cate in categories:
            print(cate.created_time)
    def test_value(self):
        categories = Category.objects.values('name')
        print(categories)

        categories = Category.objects.values_list('name', flat=True)
        print(categories)

        print(connection)

