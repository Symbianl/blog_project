# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0028_auto_20161211_1608'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(upload_to=b'article/%Y/%m', null=True, verbose_name=b'\xe9\x80\x89\xe6\x8b\xa9\xe5\x9b\xbe\xe7\x89\x87', blank=True),
        ),
    ]
