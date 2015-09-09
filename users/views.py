from django.shortcuts import render,redirect, get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from tweets.forms import TweetForm
from tweets.models import Tweet
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db.models import Q
from django.contrib.auth.models import User

from users.forms import Profile


class Profile(UpdateView):
    template_name = 'users/update_profile.html'
    model = User
    success_url = reverse_lazy('tweets_url:tweets_home')
    #fields = ['email','first_name', 'last_name']
    form_class = Profile

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.queryset = User.objects.filter(id=request.user.id)
        print request.user.id
        return super(Profile, self).dispatch(request, *args, **kwargs)
