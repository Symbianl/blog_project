# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_auto_20161005_1145'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='click_count',
            new_name='read_num',
        ),
    ]
