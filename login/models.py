import datetime
from django.db import models
from django.utils import timezone
from django.db.models import Q
from django.utils import timezone
from django.contrib.auth.models import User

class User(models.Model):
	user = models.OneToOneField(User)
	user_id = models.IntegerField(default = 0)
	player1 = models.CharField(max_length=200)
	player2 = models.CharField(max_length=200)
	player3 = models.CharField(max_length=200)
	player4 = models.CharField(max_length=200)
	player5 = models.CharField(max_length=200)

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

	def getid(self):
		return self.id

	def __str__(self):
		return self.match_name

	def test():
		return 


class Player(models.Model) :
	team = models.ForeignKey('Team')
	player_name = models.CharField(max_length=200)
	def __str__(self):
		return self.player_name

class AsignPoints(models.Model) :
	match = models.ForeignKey('Match')
	team = models.ForeignKey('Team')
	q = Match.objects.all()
	playername = models.ForeignKey('Player' )
	points = models.IntegerField(default = 0)
	def __str__(self):
		return self.match.match_name

# ,limit_choices_to= Q(team_id=q[0].team_1_id) | Q(team_id=q[0].team_2_id)
	playername = models.ForeignKey('Player')
	match = models.ForeignKey('Match')
	points = models.IntegerField(default = 0)

	def __str__(self):
		return self.match.match_name

