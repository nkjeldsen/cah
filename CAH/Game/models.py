from django.db import models

# Create your models here.

class Language(models.Model):
    name = models.CharField(max_length=50)

class WhiteCardType(models.Model):
    name = models.CharField(max_length=50)

class BlackCardType(models.Model):
    name = models.CharField(max_length=50)


class WhiteCard(models.Model):
    text      = models.CharField(max_length=500)
    language  = models.ForeignKey(Language)
    cardType  = models.ForeignKey(WhiteCardType)
    
class BlackCard(models.Model):
    text      = models.CharField(max_length=500)
    language  = models.ForeignKey(Language)
    cardType  = models.ForeignKey(BlackCardType)
    numberOfPlays = models.IntegerField(default=1,help_text="Number of white-cards required")
    
class Round(models.Model):
    BlackCard = models.ForeignKey(BlackCard)
    cardCzar  = models.ForeignKey(User)  

class ScoringMode(models.Model):
    name      = models.CharField(max_length=50)

class Game(models.Model):
    players        = models.ManyToManyField(User)
    initiatedBy    = models.ForeignKey(User) 
    numberOfRounds = models.IntegerField(default=25)
    scoringMode    = models.ForeignKey(ScoringMode)
    rounds         = models.ManyToManyField(Round) 

class Hand(models.Model):
    Users = models.ForeignKey(user)
    