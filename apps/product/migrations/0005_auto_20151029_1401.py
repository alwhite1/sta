# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20151029_1105'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='category_slug',
            new_name='category',
        ),
    ]
