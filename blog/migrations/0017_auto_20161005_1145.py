# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20161005_1009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='click_count',
            field=models.IntegerField(default=0),
        ),
    ]
