from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from hashlib import md5
from django.template.defaultfilters import linebreaksbr

class JugUser(AbstractUser):
    # Class for users. is_developer determines whether user is a developer or not
    is_developer = models.BooleanField(default=False)
    games = models.ManyToManyField('Game')

    def buyGame(self, game):
        self.games.add(game)

class Game(models.Model):
    # Class for games
    name = models.CharField(max_length=50, unique=True, default="")
    gameid = models.PositiveIntegerField(unique=True, default=10000, validators=[MinValueValidator(10000), MaxValueValidator(99999)])
    CATEGORY_CHOICES = (
        ('rpg', 'role playing'),
        ('rac', 'racing'),
        ('act', 'action'),
        ('str', 'strategy'),
        ('sho', 'shooter'),
        ('sur', 'survival'),
        ('hor', 'horror'),
        ('oth', 'other')
    )
    category = models.CharField(max_length=3, choices=CATEGORY_CHOICES)
    gameurl = models.URLField(default="http://webcourse.cs.hut.fi/example_game.html", max_length=100) 
    developer = models.ForeignKey(JugUser, on_delete=models.CASCADE)
    description = models.TextField(default="", blank=True, null=True)
    price = models.FloatField(default=0, validators=[MinValueValidator(0.0), MaxValueValidator(999)])
    sales = models.IntegerField(default=0)
    #added = models.DateTimeField(auto_now_add=True)
    highscores = models.CharField(max_length=200, default="", blank=True, null=True)


    def getRevenue(self):
        revenue = float(self.sales) * float(self.price) 
        return  str(revenue) + " €"

    def addSale(self):
        self.sales += 1
        super().save()

    def highScoreStringForHTML(self):
        try:
            hs = self.getHighScore()[0]
            hs_string =  str(hs[1]) + " - " + str(hs[0])
        except:
            hs_string = "No scores yet for this game"
        return hs_string

    def getHighScore(self):
        try:
            parsed_list = []
            for i in self.highscores.split( ): parsed_list.append((i.split(":")[0],int(i.split(":")[1])))
        except:
            # When game doesn't have scores yet just return empty list
            parsed_list = []
        return parsed_list

    def putHighScores(self, score_list):
        hs = ""
        for i in score_list: hs = hs+i[0]+":"+str(i[1])+" "
        self.highscores = hs[:-1]
        super().save()

    def saveHighScore(self, player, scores):
        hs = self.getHighScore()
        if len(hs) < 5:
            hs.append((player, int(scores)))
            hs.sort(key = lambda x: x[1], reverse=True)
        elif int(scores) > int(hs[4][1]): 
            hs.append((player, int(scores)))
            hs.sort(key = lambda x: x[1], reverse=True)
            hs = hs[:-1]
        else:
            return 1
        self.putHighScores(hs)


    def getChecksum(self):
        pid="jugment"
        sid="kikkeliskokkelis"
        secret_key="ce2e28e42ecd67eed382ca74dc65086a"
        amount=self.price
        checksumstr = "pid={}&sid={}&amount={}&token={}".format(pid, sid, amount, secret_key)
        m = md5(checksumstr.encode("ascii"))
        checksum = m.hexdigest()

        return checksum

class GameSave(models.Model):
    # Class for handling user gamesaves
    game = models.ForeignKey(Game, on_delete=models.CASCADE, null=True)
    player = models.ForeignKey(JugUser, on_delete=models.CASCADE, null=True)

    # user scores
    scores = models.CharField(max_length=100, default="", null=True)

    # game saves
    gamestate = models.CharField(max_length=500, default="", null=True)


    def getHighScore(self):
        return self.scores.split("\n")[0]

    def getScores(self):
        return self.scores

    def addScores(self, newScores):
        if self.scores == "":
            self.scores = newScores + "\n"
        else:
            lines = self.scores.split("\n")

            # Remove excess empty line
            lines = lines[:-1]
                
            lines.append(newScores)
            lines = [int(line) for line in lines]
            lines = sorted(lines, reverse=True)
            
            # Only keep top 5 scores
            if len(lines) > 5:
                lines = lines[:-1]
            self.scores = ""
            for line in lines:
                self.scores += str(line) + "\n"
        self.game.saveHighScore(str(self.player), newScores)