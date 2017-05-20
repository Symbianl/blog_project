# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_auto_20161024_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='read_num',
            field=models.IntegerField(default=0, verbose_name=b'\xe6\xb5\x8f\xe8\xa7\x88\xe6\x95\xb0\xe7\x9b\xae'),
        ),
    ]
