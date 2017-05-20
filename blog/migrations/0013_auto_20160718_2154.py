# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20160718_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='read_num',
            field=models.IntegerField(default=1),
        ),
    ]
