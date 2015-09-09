# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0005_auto_20150908_2014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='name',
        ),
    ]
