from django.contrib.auth.models import User
from django.db import connection
from django.test import TestCase


from .models import Category

class TestCategory(TestCase):
    def setUp(self):
        user = User.objects.create_user('the5fire', 'fake@email.com', 'password')
        for i in range(10):
            category_name = 'cate_%s' % i
            Category.objects.create(name=category_name, owner=user)



    def test_filter(self):
        queryset = Category.objects.all()
        print(type(queryset))
        categories = queryset.filter(status=1)
        print(type(categories))
        categories = queryset.exclude(status=0)
        print(type(categories))