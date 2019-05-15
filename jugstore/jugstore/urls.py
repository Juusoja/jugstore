"""jugstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from jugstore.jstore import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Accounts urlit avautuu automaattisesti jos käyttäjä menee etusivulle kirjautumattomana
    path('accounts/', include('jugstore.jstore.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    # Pääsivu (Vaihdetaan myöhemmin rootiksi)
    path('', views.home, name="home"),
    # Pelikauppanäkymä, ostettavissa olevat pelit listattuna
    path('gamestore', views.gamestore, name='gamestore'),
    path('gamestore/buy/<g>', views.buygame, name='buygame'),
    path('leaderboards', views.leaderboards, name='leaderboards'),
    path('addgame', views.addgame, name='addgame'),
    path('savegame', views.savegame, name='savegame'),
    path('errorpage', views.errorpage, name='errorpage'),
    path('removegame', views.removegame, name='removegame'),
    path('editgame/<g>/', views.editgame, name='editgame'),
]
