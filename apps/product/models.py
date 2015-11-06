# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from pytils.translit import slugify


class Category(models.Model):

    name = models.CharField(max_length=32, unique=True)
    slug = models.SlugField(unique=True, editable=False)
    description = models.TextField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name).replace('-', '_')
        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product:category_products', kwargs={'category_slug': self.slug})


class Product(models.Model):

    name = models.CharField(max_length=32)
    slug = models.SlugField(unique=True, editable=False)
    description = models.TextField()
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(to=Category, to_field='slug')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name).replace('-', '_')
        super(Product, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product:single_product', kwargs={'category_slug': self.category.slug, 'product_slug': self.slug})[:-1]
