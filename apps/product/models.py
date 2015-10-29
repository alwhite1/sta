# -*- coding: utf-8 -*-
import datetime
from django.db import models
from pytils.translit import slugify


class Category(models.Model):

    name = models.CharField(max_length=32, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name).replace(' ', '_')
        super(Category, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name


class Product(models.Model):

    name = models.CharField(max_length=32)
    slug = models.SlugField()
    description = models.TextField()
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(blank=True, null=True)
    category = models.ForeignKey(to=Category, to_field='slug')

    def save(self, *args, **kwargs):
        self.modified_at = datetime.datetime.now()
        self.slug = slugify(self.name).replace(' ', '_')
        super(Product, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name
