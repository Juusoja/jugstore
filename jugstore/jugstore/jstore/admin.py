from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import JugUserCreationForm, JugUserChangeForm
from .models import JugUser, Game, GameSave

class JugUserAdmin(UserAdmin):
    add_form = JugUserCreationForm
    form = JugUserChangeForm
    model = JugUser
    list_display = ['email', 'username',"is_developer"]

admin.site.register(JugUser, JugUserAdmin)
admin.site.register(Game)
admin.site.register(GameSave)