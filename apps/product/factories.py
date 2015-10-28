# -*- coding: utf-8 -*-
import factory
from .models import Category, Product


class CategoryFactory(factory.Factory):

    class Meta:
        model = Category

    name = "Test"
    slug = "test"
    description = "test"


class CyrillicCategoryFactory(factory.Factory):

    class Meta:
        model = Category

    name = u"тест"
    slug = u"тест"
    description = u"тест"


class ProductFactory(factory.Factory):

    class Meta:
        model = Product

    name = "test"
    slug = "test"
    description = "test"
    price = "12"
    category_id = 1


class CyrillicProductFactory(factory.Factory):

    class Meta:
        model = Product

    name = u"тест"
    slug = u"тест"
    description = u"тест"
    price = 12
    category_id = 1
