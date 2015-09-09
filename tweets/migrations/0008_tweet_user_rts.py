# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tweets', '0007_retweet'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='user_rts',
            field=models.ManyToManyField(related_name='user_rts', through='tweets.ReTweet', to=settings.AUTH_USER_MODEL),
        ),
    ]
