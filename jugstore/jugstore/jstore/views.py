from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.views import generic
from django.views.decorators.csrf import csrf_protect
from .forms import JugUserCreationForm, GameAddForm, GameEditForm
from .models import Game, JugUser, GameSave
from django.shortcuts import get_object_or_404
import datetime


@login_required
def home(request):
    # Main view, separate pages for developers and players
    if request.user.is_developer:
        games = Game.objects.all()
        mygames = []
        for game in games:
            if game.developer == request.user:
                mygames.append(game)
        return render(request, "developerhome.html", {'mygames':mygames})
    else:
        return render(request, "playerhome.html")

@login_required
def gamestore(request):
    tempgames = Game.objects.all() 
    usergames = request.user.games.all()
    games = []
    for game in tempgames:
        if not game in usergames:
            games.append(game)
    return render(request, "gamestore.html", {'games':games}, {'user':request.user})


@login_required
def leaderboards(request):
    return render(request, "leaderboards.html")


@login_required
def buygame(request, g):
    # Buy games into game catalog
    user = request.user
    
    # Add a game for user
    game = Game.objects.get(gameid=g)    
    user.buyGame(game)
    game.addSale()
    game.save()
    user.save()

    # Create a new gamesave model
    gamesave = GameSave(game = game, player = user)
    gamesave.save()

    return HttpResponseRedirect('/')


@login_required
def errorpage(request):
    return HttpResponse('<h1>Error trying to buy a game. Try again later or contact admin. </h1>  <a href="/home" >Go back to store</a>')
    

@login_required
def addgame(request):
    # Adding games to gamestore (developer)
    if request.user.is_developer:
        if request.method == 'GET':
            add_form = GameAddForm()
            return render(request, 'addgame.html', {'add_form': add_form})
        elif request.method == 'POST':
            user = JugUser.objects.get(username=request.user)
            add_game_form = GameAddForm(data=request.POST)
            if add_game_form.is_valid():
                game = Game(gameid=10001+Game.objects.all().count(),
                        name=add_game_form.cleaned_data['name'],
                        category=add_game_form.cleaned_data['category'],
                        description=add_game_form.cleaned_data['description'],
                        price=add_game_form.cleaned_data['price'],
                        developer=user)
                game.save()
            else:
                print(add_game_form)
        return HttpResponseRedirect("/")
    else:
        return HttpResponse('<h1>You have no business here, you are not a jugeloper </h1>  <a href="/" >Go back to store</a>')

@login_required
def editgame(request, g):
    # Editing games to gamestore (developer)
    if request.user.is_developer:
        if request.method == 'GET':
            edit_game_form = GameEditForm()
            return render(request, 'editgame.html', {'id':g}, {'edit_game_form': edit_game_form})
        elif request.method == 'POST':
            gid = g
            edit_game_form = GameEditForm(data=request.POST)
            if edit_game_form.is_valid():
                if JugUser.objects.get(username=request.user) == Game.objects.get(gameid=gid).developer:
                    if edit_game_form.cleaned_data['name']:
                        Game.objects.filter(gameid=gid).update(name=edit_game_form.cleaned_data['name'])
                    if edit_game_form.cleaned_data['description']:
                        Game.objects.filter(gameid=gid).update(description=edit_game_form.cleaned_data['description'])
                    Game.objects.get(gameid=gid).save()
                else:
                    return HttpResponse('<h1>Error modifying game, try again later or contact system admin </h1>  <a href="/" >Go back to screen </a>')
            else:
                return HttpResponse('<h1>Game Form is invalid, please contact system admin </h1>  <a href="/" >Go back to screen </a>')
            return HttpResponseRedirect("/")
    else:
        return HttpResponse('<h1>You have no business here, you are not a jugeloper </h1>  <a href="/" >Go back to store</a>')


@csrf_protect
@login_required
def removegame(request):
    # Removing games from gamestore (developer)
    if request.user.is_developer:
        gid = request.POST['gid']
        if request.method == 'POST':
            user = JugUser.objects.get(username=request.user)
            if user == Game.objects.get(gameid=gid).developer:
                Game.objects.get(gameid=gid).delete()
            return HttpResponseRedirect("/")
        else:
            return HttpResponseRedirect("/")
    else:
        return HttpResponse('<h1>You have no business here, you are not a jugeloper </h1>  <a href="/home" >Go back to store</a>')



@csrf_protect
@login_required
def savegame(request):
    # Method for saving gamestate
    user = request.user
    gid = request.POST['gid']
    game = Game.objects.get(gameid=gid)
    gamesave = GameSave.objects.get(player=user, game=game)
    print("Saving game...")
    if request.method == 'POST':
        print("Got post request")
        # Pelitilanne vastaanotettu 
        if request.POST.get('messageType') == 'SAVE':
            print("Got save type")
            gamesave.gamestate = request.POST.get('gamestate')
            print(gamesave.gamestate)
            gamesave.save()
            print("Game saved")
        # Pisteet vastaanotettu
        elif request.POST.get('messageType') == 'SCORE':
            print("Got score type")
            gamesave.addScores(request.POST.get('score'))
            gamesave.save()
    return HttpResponseRedirect("/")


class SignUp(generic.CreateView):
    form_class = JugUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"