# -*- coding: utf-8 -*-
from django.test import TestCase
from django.core.urlresolvers import resolve
from apps.product.views import get_categories
from apps.product.models import Category


class GetCategoriesViewTest(TestCase):

    def test_can_resolve_categories_page(self):
        found = resolve('/product/')
        self.assertEqual(found.func, get_categories)

    def test_what_template_used_to_categories_page(self):
        response = self.client.get('/product/')
        self.assertTemplateUsed(response, 'categories.html')

    def test_can_categories_page_load_if_db_is_empty(self):
        self.assertEqual(Category.objects.count(), 0)
        response = self.client.get('/product/')
        self.assertEqual(response.status_code, 200)

    def test_cyrillic_rendering(self):
        Category(name=u'тест', description=u'тест').save()
        self.assertEqual(Category.objects.count(), 1)
        response = self.client.get('/product/')
        self.assertEqual(response.context['categories'][0].name, u'тест')

    def test_multiple_objects_rendering(self):
        Category.objects.all().delete()
        Category(name=u'тест', description=u'тест').save()
        Category(name=u'тест 1', description=u'тест 1').save()
        self.assertEqual(Category.objects.count(), 2)
        response = self.client.get('/product/')
        self.assertEqual(len(response.context['categories']), 2)
