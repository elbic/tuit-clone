from django.shortcuts import render,redirect, get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from tweets.forms import TweetForm
from tweets.models import Tweet, Favorite, ReTweet
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db.models import Q


# def new_tweet(request):
#     #return HttpResponse('hola', content_type='text/plain')
#     if request.method == 'POST':
#         form  = TweetForm(request.POST)
#
#         if form.is_valid():
#             form.save()
#             return HttpResponse('guardado')
#         else:
#             return render(request, 'tweets/create_tweet.html',{'tweet_form': form})
#
#     form = TweetForm()
#     return render(request, 'tweets/create_tweet.html',{'tweet_form': form})
#

class AddTweet(CreateView):
    template_name = 'tweets/create_tweet.html'
    model = Tweet
    form_class = TweetForm
    success_url = reverse_lazy('tweets_url:tweets_home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AddTweet, self).form_valid(form)

# def show_tweet(request, id_tweet):
#
#     # try:
#     #     tweet = Tweet.objects.get(id=id_tweet)
#     # except Tweet.DoesNotExist:
#     #     raise Http404('Ese tweet no existe')
#     tweet  = get_object_or_404(Tweet, id=id_tweet)
#     return render(request, 'tweets/show_tweet.html',{'tweet': tweet})

class ShowTweet(ListView):
    template_name = 'tweets/show_tweet.html'
    context_object_name = 'tweet'
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.queryset = Tweet.objects.filter(id=self.kwargs['id_tweet']).first()
        return super(ShowTweet, self).dispatch(request, *args, **kwargs)


def tweet_login(request):
    template_response = 'tweets/login.html'
    if request.method=='POST':
        form = AuthenticationForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect(reverse('tweets_url:tweets_home'))
        else:
            messages.error(request, u'Usuario/Password incorrecto')
            return render(request, template_response, {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, template_response, {'form': form})

def tweet_logout(request):
    logout(request)
    return redirect(reverse('tweets_url:tweets_home'))

# def list_tweets(request):
#     # list_tweets = Tweet.objects.all()
#     list_tweets = get_list_or_404(Tweet)
#     return render(request, 'tweets/list_tweets.html',{'list_tweets': list_tweets})

class ListTweets(ListView):
    template_name = 'tweets/list_tweets.html'
    context_object_name = 'list_tweets'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.queryset = Tweet.objects.filter(~Q(user=request.user)).order_by('-date')
        return super(ListTweets, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ListTweets, self).get_context_data(**kwargs)
        context['user_favs'] = Favorite.objects.filter(user=self.request.user).values_list('tweet__id', flat=True)
        context['user_rts'] = ReTweet.objects.filter(user=self.request.user).values_list('tweet__id', flat=True)
        return context



# def delete_tweet(request, id_tweet):
#     Tweet.objects.filter(id=id_tweet).delete()
#     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

class DeleteTweet(DeleteView):
    model = Tweet
    form_class = TweetForm
    success_url = reverse_lazy('tweets_url:timeline')
    slug_field = 'id'
    slug_url_kwarg = 'id_tweet'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.queryset = Tweet.objects.filter(id=self.kwargs['id_tweet'])
        request.method = 'POST'
        return super(DeleteTweet, self).dispatch(request, *args, **kwargs)

# def edit_tweet(request, id_tweet):
#     tweet  = get_object_or_404(Tweet, id=id_tweet)
#
#     if request.method == 'POST':
#         form  = TweetForm(request.POST, instance=tweet)
#
#         if form.is_valid():
#             form.save()
#             return HttpResponse('guardado')
#         else:
#             return render(request, 'tweets/update_tweet.html',{'tweet_form': form})
#
#     form = TweetForm(instance=tweet)
#     return render(request, 'tweets/update_tweet.html',{'tweet_form': form})

class EditTweet(UpdateView):
    template_name = 'tweets/update_tweet.html'
    form_class = TweetForm
    success_url = reverse_lazy('tweets_url:timeline')
    slug_field = 'id'
    slug_url_kwarg = 'id_tweet'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.queryset = Tweet.objects.filter(id=self.kwargs['id_tweet'])
        return super(EditTweet, self).dispatch(request, *args, **kwargs)

class TimeLine(ListView):
    template_name = 'tweets/timeline.html'
    context_object_name = 'list_tweets'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.queryset = Tweet.objects.filter(Q(user=request.user)).order_by('-date')
        return super(TimeLine, self).dispatch(request, *args, **kwargs)


class CreateFavorite(View):
    def get(self, request, id_tweet):
        try:
            tweet = get_object_or_404(Tweet, ~Q(user=request.user), id=id_tweet)
            favorite, create = Favorite.objects.get_or_create(user=request.user, tweet=tweet)
        except:
            messages.warning(request, 'No puedes favoritear el tuit')
            return redirect(reverse('tweets_url:tweets_home'))

        messages.success(request, 'Marcado como favorito')
        return redirect(reverse('tweets_url:tweets_home'))

class DeleteFavorite(View):
    def get(self, request, id_tweet):
        try:
            tweet = get_object_or_404(Tweet, ~Q(user=request.user), id=id_tweet)
            get_object_or_404(Favorite, user=request.user, tweet=tweet).delete()
        except:
            messages.warning(request, 'No se puede eliminar favorito')
            return redirect(reverse('tweets_url:tweets_home'))

        messages.success(request, 'Favorito borrado')
        return redirect(reverse('tweets_url:tweets_home'))


class CreateRT(View):
    def get(self, request, id_tweet):
        try:
            tweet = get_object_or_404(Tweet, ~Q(user=request.user), id=id_tweet)
            rt, create = ReTweet.objects.get_or_create(user=request.user, tweet=tweet)
        except:
            messages.warning(request, 'No se puede retuitear')
            return redirect(reverse('tweets_url:tweets_home'))

        messages.success(request, 'RT!')
        return redirect(reverse('tweets_url:tweets_home'))

class DeleteRT(View):
    def get(self, request, id_tweet):
        try:
            tweet = get_object_or_404(Tweet, ~Q(user=request.user), id=id_tweet)
            get_object_or_404(ReTweet, user=request.user, tweet=tweet)
        except:
            messages.warning(request, 'No se puede eliminar el RT')
            return redirect(reverse('tweets_url:tweets_home'))

        messages.success(request, 'RT Eliminado')
        return redirect(reverse('tweets_url:tweets_home'))


class ListFavorites(ListView):
    template_name = 'tweets/list_favorites.html'
    context_object_name = 'favorites'
    slug_field = 'id'
    slug_url_kwarg = 'id_tweet'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.queryset = Tweet.objects.filter(Q(id=self.kwargs['id_tweet'])).first()
        return super(ListFavorites, self).dispatch(request, *args, **kwargs)

class ListRetweets(ListView):
    template_name = 'tweets/list_retweets.html'
    context_object_name = 'favorites'
    slug_field = 'id'
    slug_url_kwarg = 'id_tweet'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.queryset = Tweet.objects.filter(Q(id=self.kwargs['id_tweet'])).first()
        return super(ListRetweets, self).dispatch(request, *args, **kwargs)
