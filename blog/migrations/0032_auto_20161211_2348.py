# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0031_read'),
    ]

    operations = [
        migrations.RenameField(
            model_name='read',
            old_name='image',
            new_name='image_s',
        ),
    ]
