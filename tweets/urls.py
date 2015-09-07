from django.conf.urls import url
from tweets.views import ListTweets, AddTweet, ShowTweet, EditTweet, DeleteTweet, TimeLine

urlpatterns = [
    url(r'^$', ListTweets.as_view(), name='tweets_home'),
    url(r'^add_tweet/$', AddTweet.as_view(), name='add_tweet'),
    url(r'^tweet/(?P<id_tweet>\d{1,})/$', ShowTweet.as_view(), name='tweet_message'),
    url(r'^delete/(?P<id_tweet>\d{1,})/$', DeleteTweet.as_view(), name='delete_tweet'),
    url(r'^edit_tweet/(?P<id_tweet>\d{1,})/$', EditTweet.as_view(), name='edit_tweet'),
    url(r'^timeline/$', TimeLine.as_view(), name='timeline'),
]
