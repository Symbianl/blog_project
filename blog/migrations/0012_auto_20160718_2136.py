# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_remove_article_click_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='read_num',
            field=models.IntegerField(default=0),
        ),
    ]
