# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tweets', '0004_tweet_tweet_favs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='tweet_favs',
        ),
        migrations.AddField(
            model_name='tweet',
            name='user_favs',
            field=models.ManyToManyField(related_name='user_favs', through='tweets.Favorite', to=settings.AUTH_USER_MODEL),
        ),
    ]
