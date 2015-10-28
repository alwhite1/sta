from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=32)
    slug = models.SlugField()
    description = models.TextField()

    def __unicode__(self):
        return self.name


class Product(models.Model):

    name = models.CharField(max_length=32)
    slug = models.SlugField()
    description = models.TextField()
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(blank=True, null=True)
    category_id = models.IntegerField()

    def __unicode__(self):
        return self.name
