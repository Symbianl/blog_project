# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0033_auto_20161217_2258'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='read',
            options={'ordering': ['index', 'id', '-date_publish'], 'verbose_name': '\u7ad9\u957f\u63a8\u8350', 'verbose_name_plural': '\u7ad9\u957f\u63a8\u8350'},
        ),
        migrations.AddField(
            model_name='read',
            name='index',
            field=models.IntegerField(default=999, verbose_name=b'\xe6\x8e\x92\xe5\x88\x97\xe9\xa1\xba\xe5\xba\x8f(\xe4\xbb\x8e\xe5\xb0\x8f\xe5\x88\xb0\xe5\xa4\xa7)'),
        ),
    ]
