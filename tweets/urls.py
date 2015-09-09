from django.conf.urls import url
from tweets.views import ListTweets, AddTweet, ShowTweet, EditTweet, DeleteTweet, TimeLine, CreateFavorite, DeleteFavorite, CreateRT, DeleteRT, ListFavorites, ListRetweets

urlpatterns = [
    url(r'^$', ListTweets.as_view(), name='tweets_home'),
    url(r'^add_tweet/$', AddTweet.as_view(), name='add_tweet'),
    url(r'^tweet/(?P<id_tweet>\d{1,})/$', ShowTweet.as_view(), name='tweet_message'),
    url(r'^delete/(?P<id_tweet>\d{1,})/$', DeleteTweet.as_view(), name='delete_tweet'),
    url(r'^edit_tweet/(?P<id_tweet>\d{1,})/$', EditTweet.as_view(), name='edit_tweet'),
    url(r'^timeline/$', TimeLine.as_view(), name='timeline'),

    url(r'^favorite/(?P<id_tweet>\d{1,})/$', CreateFavorite.as_view(), name='favorite'),
    url(r'^favorite/delete/(?P<id_tweet>\d{1,})/$', DeleteFavorite.as_view(), name='del_fav'),

    url(r'^retweet/(?P<id_tweet>\d{1,})/$', CreateRT.as_view(), name='add_rt'),
    url(r'^retweet/delete/(?P<id_tweet>\d{1,})/$', DeleteRT.as_view(), name='del_rt'),

    url(r'^list_favorites/(?P<id_tweet>\d{1,})/$', ListFavorites.as_view(), name='list_favorites'),
    url(r'^list_retweets/(?P<id_tweet>\d{1,})/$', ListRetweets.as_view(), name='list_retweets'),


]
