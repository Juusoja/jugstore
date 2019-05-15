from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import JugUser
from .models import Game

class JugUserCreationForm(UserCreationForm):
    # Register form
    class Meta(UserCreationForm):
        model = JugUser
        fields = ('username', 'email', 'is_developer')

class JugUserChangeForm(UserChangeForm):
    # User information modification form
    class Meta:
        model = JugUser
        fields = ('username', 'email')

class GameAddForm(forms.ModelForm):
    # Game add form
    class Meta:
        model = Game
        fields = ('name', 'description', 'category', 'price')

class GameEditForm(forms.ModelForm):
    # Game add form
    class Meta:
        model = Game
        fields = ('name', 'description')