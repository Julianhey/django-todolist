from django import forms
from .models import Todo, Comment, GameInstance
import urllib.request
import urllib.parse
import json

api = 'https://igdbcom-internet-game-database-v1.p.mashape.com/'
request = {}

class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ('title', 'text',)

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)

class GameForm(forms.ModelForm):

    class Meta:
        model = GameInstance
        fields = ('title', 'platform')

    """def clean(self):
        if(self.cleaned_data.get('title') != Gamelist):

            raise ValidationError(
            "Unkown Game, please select a suggested option"
            )

        if(self.cleaned_data.get('platform') != Platfromlist):

            raise ValidationError(
            "Unkown Platform, please select a suggested option"
            )"""
