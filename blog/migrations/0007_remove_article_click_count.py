# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20160602_1114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='click_count',
        ),
    ]
