"""twitter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
# from tweets.views import new_tweet,show_tweet, delete_tweet, edit_tweet
from tweets.views import tweet_login, tweet_logout
from users.views import Profile
from tweets import urls as tweets_url
from django.conf import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tweet/', include(tweets_url, namespace='tweets_url')),
    url(r'^tweet/login/$', tweet_login, name='tweet_login'),
    url(r'^tweet/logout/$', tweet_logout, name='tweet_logout'),
    url(r'^tweet/update_profile/(?P<pk>\d{1,})/$', Profile.as_view(), name='update_profile'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
