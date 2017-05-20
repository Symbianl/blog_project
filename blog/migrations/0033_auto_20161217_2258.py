# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0032_auto_20161211_2348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='read',
            name='desc',
        ),
        migrations.RemoveField(
            model_name='read',
            name='image_s',
        ),
    ]
