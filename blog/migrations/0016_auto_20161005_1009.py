# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20160718_2204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='read_num',
        ),
        migrations.AddField(
            model_name='article',
            name='click_count',
            field=models.IntegerField(default=0, verbose_name=b'\xe7\x82\xb9\xe5\x87\xbb\xe6\xac\xa1\xe6\x95\xb0'),
        ),
    ]
