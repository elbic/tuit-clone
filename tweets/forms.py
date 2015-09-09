from django import forms
from tweets.models import Tweet, Favorite

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['tweet']
        widgets = {
            "tweet" : forms.TextInput(attrs={"class" : "form-control"}),
        }


class FavoriteForm(forms.ModelForm):
    class Meta:
        model = Favorite
        exclude = ['date','user', 'tweet']
