from django.test import TestCase
from apps.product.factories import ProductFactory, CategoryFactory, CyrillicProductFactory, CyrillicCategoryFactory
from apps.product.models import Category, Product


class CategoryModelTest(TestCase):

    def test_can_create_new_object(self):
        CategoryFactory.create().save()
        self.assertEqual(Category.objects.count(), 1)

    def test_can_delete_object(self):
        Category.objects.all().delete()
        self.assertEqual(Category.objects.count(), 0)

    def test_cyrillic_support(self):
        CyrillicCategoryFactory.create().save()
        self.assertEqual(Category.objects.count(), 1)


class ProductModelTest(TestCase):

    def test_can_create_new_object(self):
        ProductFactory.create().save()
        self.assertEqual(Product.objects.count(), 1)

    def test_can_delete_object(self):
        Product.objects.all().delete()
        self.assertEqual(Product.objects.count(), 0)

    def test_cyrillic_support(self):
        CyrillicProductFactory.create().save()
        self.assertEqual(Product.objects.count(), 1)
