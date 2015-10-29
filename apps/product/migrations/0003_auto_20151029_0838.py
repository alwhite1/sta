# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20151028_1510'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category_id',
        ),
        migrations.AddField(
            model_name='product',
            name='category_slug',
            field=models.CharField(default=b'None', max_length=64, choices=[('Test Category 1', 'test_category_1'), ('Test Category 2', 'test_category_2')]),
        ),
    ]
