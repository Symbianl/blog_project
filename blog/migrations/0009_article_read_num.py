# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_article_click_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='read_num',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
