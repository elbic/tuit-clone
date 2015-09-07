from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tweet(models.Model):
    name = models.CharField(max_length=15)
    tweet = models.CharField(max_length=140)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
    
    def __unicode__(self):
        return "{0} - {1}".format(self.user, self.date)
