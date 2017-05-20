# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_auto_20161103_2133'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['-id'], 'verbose_name': '\u540e\u53f0\u7528\u6237', 'verbose_name_plural': '\u540e\u53f0\u7528\u6237'},
        ),
        migrations.AlterModelOptions(
            name='user_x',
            options={'ordering': ['id'], 'verbose_name': '\u6ce8\u518c\u7528\u6237', 'verbose_name_plural': '\u6ce8\u518c\u7528\u6237'},
        ),
    ]
