# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tweets', '0003_favorite'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='tweet_favs',
            field=models.ManyToManyField(related_name='tweet_favorite', through='tweets.Favorite', to=settings.AUTH_USER_MODEL),
        ),
    ]
