# -*- coding: utf-8 -*-
from django.test import TestCase
from apps.product.models import Category, Product


class CategoryModelTest(TestCase):

    def test_can_create_new_object(self):
        Category(name='test', description='test').save()
        self.assertEqual(Category.objects.count(), 1)

    def test_can_delete_object(self):
        Category.objects.all().delete()
        self.assertEqual(Category.objects.count(), 0)

    def test_cyrillic_support(self):
        Category(name=u'тест', description=u'тест').save()
        self.assertEqual(Category.objects.count(), 1)


class ProductModelTest(TestCase):

    def test_can_create_new_object(self):
        Category(name='test', description='test').save()
        Product(name='test', description='test', category=Category.objects.last(), price=15).save()
        self.assertEqual(Product.objects.count(), 1)

    def test_can_delete_object(self):
        Product.objects.all().delete()
        self.assertEqual(Product.objects.count(), 0)

    def test_cyrillic_support(self):
        Category(name='test', description='test').save()
        Product(name=u'тест', description=u'тест', category=Category.objects.last(), price=15).save()
        self.assertEqual(Product.objects.count(), 1)
