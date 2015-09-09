from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tweet(models.Model):
    tweet = models.CharField(max_length=140)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    user_favs = models.ManyToManyField(User, through='tweets.Favorite', related_name='user_favs')
    user_rts = models.ManyToManyField(User, through='tweets.ReTweet', related_name='user_rts')

    def __unicode__(self):
        return "{0} - {1}".format(self.user, self.date)

class Favorite(models.Model):
    user = models.ForeignKey(User)
    tweet = models.ForeignKey('tweets.Tweet')
    date = models.DateTimeField(auto_now_add=True)


class ReTweet(models.Model):
    user = models.ForeignKey(User)
    tweet = models.ForeignKey('tweets.Tweet')
    date = models.DateTimeField(auto_now_add=True)
