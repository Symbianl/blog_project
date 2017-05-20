# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_auto_20161117_2212'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_x',
            name='sex',
            field=models.CharField(blank=True, max_length=10, null=True, choices=[(b'male', b'\xe7\x94\xb7'), (b'female', b'\xe5\xa5\xb3')]),
        ),
    ]
