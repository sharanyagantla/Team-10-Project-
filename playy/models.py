from django.db import models
import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Team(models.Model):
	team_name = models.CharField(max_length=200)
	def __str__(self):              # __unicode__ on Python 2
		return self.team_name

class Match(models.Model):
	match_name = models.CharField(max_length=200)
	team_1 = models.ForeignKey('Team', related_name = 'team1')
	team_2 = models.ForeignKey('Team', related_name = 'team2')
	pub_date = models.DateTimeField('date of match')
	def __str__(self):
		return self.match_name


class Player(models.Model) :
	team = models.ForeignKey('Team')
	player_name = models.CharField(max_length=200)

	def __str__(self):              # __unicode__ on Python 2
		return self.player_name
