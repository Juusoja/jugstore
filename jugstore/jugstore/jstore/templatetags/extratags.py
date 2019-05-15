from django import template
from ..models import GameSave, Game
from django.template.defaultfilters import linebreaksbr
register = template.Library()

@register.simple_tag
def getGameState(player, game):
    try:
        gamesave = GameSave.objects.get(player=player, game=game).gamestate
    except:
        gamesave = "(No game saves yet)"
    return gamesave

@register.simple_tag
def getUserHighScore(player, game):
    try:
        gamesave = GameSave.objects.get(player=player, game=game)
        scores = gamesave.getHighScore()
    except:
        scores = "(No scores yet)"
    return scores

@register.simple_tag
def getUserScores(player, game):
    try:
        gamesave = GameSave.objects.get(player=player, game=game)
        scores = gamesave.getScores()
        while (len(scores.split("\n")) < 6):
            scores += "\n"
        scores = linebreaksbr(scores)
    except:
        scores = "-"
    return scores

@register.simple_tag
def getGlobalScores(gameid):
    try:
        game = Game.objects.get(gameid=gameid)
        scorestemp = game.highscores.replace(" ", "\n").split("\n")
        scores = ""
        for score in scorestemp:
            scores += score.split(":")[1] + " - " + score.split(":")[0] + "\n"
        while (len(scores.split("\n")) < 6):
            scores += "\n"
        scores = linebreaksbr(scores)
    except:
        scores = "-"
    return scores

@register.simple_tag
def getGameStoreCount(gameslist):
    return len(gameslist)

@register.simple_tag
def getDevSales(developer):
    try:
        games = Game.objects.all()
        sales = 0
        for game in games:
            if game.developer == developer:
                sales += game.sales
    except:
        sales = "Error"
    return sales

@register.simple_tag
def getDevRevenue(developer):
    try:
        games = Game.objects.all()
        revenue = 0
        for game in games:
            if game.developer == developer:
                revenue += float(game.sales) * float(game.price) 
    except:
        revenue = "Error"
    return str(revenue) + " €"


@register.simple_tag
def getGameName(id):
    game = Game.objects.get(gameid=id)
    return game.name


@register.simple_tag
def getGamePrice(id):
    game = Game.objects.get(gameid=id)
    return game.price

@register.simple_tag
def getGameDescription(id):
    game = Game.objects.get(gameid=id)
    return game.description





