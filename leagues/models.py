from __future__ import unicode_literals

from django.db import models

class Player(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    user_name = models.CharField(max_length=30)
    password = models.CharField(max_length=50)
    photo = models.ImageField()

class Team(models.Model):
    team_name = models.CharField(max_length=30)
    team_color = models.CharField(max_length=30)
    is_active = models.BooleanField()

class Roster(models.Model):
	player = models.ForeignKey(Player, on_delete=models.CASCADE)
	team = models.ForeignKey(Team, on_delete=models.CASCADE)
    position1 = models.CharField(max_length=30)
    position2 = models.CharField(max_length=30)

class Season(models.Model):
	team = models.ForeignKey(Team, on_delete=models.CASCADE)
    is_champion = models.NullBooleanField()

class League(models.Model):
	season = models.ForeignKey(Season)
	team = models.ForeignKey(Team)
	division = models.PositiveSmallIntegerField()
	win = models.PositiveSmallIntegerField()
	loss = models.PositiveSmallIntegerField()
	tie = models.PositiveSmallIntegerField()
	goals_for = models.PositiveSmallIntegerField()
	goals_against = models.PositiveSmallIntegerField()

class Games(models.Model):
	season = models.ForeignKey(Season)
	date = models.DateField()
	time = models.TimeField()
	awayteam = models.ForeignKey(Team)
	hometeam = models.ForeignKey(Team)
	ref1 = models.CharField(max_length=50)
	ref2 = models.CharField(max_length=50)
	notes = models.CharField(max_length=500)
	is_regularseasion = models.BooleanField()


class Stats(models.Model):
	season = models.ForeignKey(Season)
	player = models.ForeignKey(Player, on_delete=models.CASCADE)
	game = models.ForeignKey(Games)
	assists = models.PositiveSmallIntegerField()
	goals_against = models.PositiveSmallIntegerField()
	en = models.PositiveSmallIntegerField()

class Refs(models.Model):
	first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    plaer = models.ForeignKey(Player)