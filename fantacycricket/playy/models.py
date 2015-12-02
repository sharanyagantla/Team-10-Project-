from django.db import models
import datetime
from django.db import models
from django.utils import timezone
from django.db.models import Q
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
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
	def __str__(self):
		return self.player_name


class AsignPoints(models.Model ) :
	match = models.ForeignKey('Match')
	playername = models.ForeignKey('Player')
	points = models.IntegerField(default = 0)

	def __str__(self):
		return self.playername.player_name 


class UserProfile(models.Model):
	class Meta:
		unique_together = ['user', 'match']
	user = models.ForeignKey(User)
	match = models.ForeignKey('Match')
	player_1 = models.ForeignKey('Player' , related_name = 'player1')
	player_2 = models.ForeignKey('Player' , related_name = 'player2')
	player_3 = models.ForeignKey('Player' , related_name = 'player3')
	player_4 = models.ForeignKey('Player' , related_name = 'player4')
	player_5 = models.ForeignKey('Player' , related_name = 'player5')
	total_points = models.IntegerField(default=0)

	def __str__(self):
		return self.user.username +" for "+ self.match.match_name

class Points(models.Model):
	user = models.ForeignKey(User)
	full_points = models.IntegerField(default = 0)

	def __str__(self):
		return self.user.username
