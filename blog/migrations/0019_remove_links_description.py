# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20161005_1200'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='links',
            name='description',
        ),
    ]
