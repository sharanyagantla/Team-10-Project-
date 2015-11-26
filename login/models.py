from django.db import models
<<<<<<< HEAD
import datetime
from django.db import models
from django.utils import timezone
from django.db.models import Q
=======
<<<<<<< HEAD
import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
>>>>>>> d1c94c9d04de9168cc110551037b0345be010529

class Team(models.Model):
	team_name = models.CharField(max_length=200)
	def __str__(self):              # __unicode__ on Python 2
		return self.team_name

class Match(models.Model):
	match_name = models.CharField(max_length=200)
	team_1 = models.ForeignKey('Team', related_name = 'team1')
	team_2 = models.ForeignKey('Team', related_name = 'team2')
	pub_date = models.DateTimeField('date of match')
<<<<<<< HEAD

	def __str__(self):
		return self.match_name

	def getid(self):
		return self.id
=======
	def __str__(self):
		return self.match_name

	def test():
		return 
>>>>>>> d1c94c9d04de9168cc110551037b0345be010529

class Player(models.Model) :
	team = models.ForeignKey('Team')
	player_name = models.CharField(max_length=200)
	def __str__(self):
		return self.player_name


class AsignPoints(models.Model) :
<<<<<<< HEAD
	match = models.ForeignKey('Match')
	team = models.ForeignKey('Team')
	q = Match.objects.all()
	playername = models.ForeignKey('Player' )
	points = models.IntegerField(default = 0)
	def __str__(self):
		return self.match.match_name

# ,limit_choices_to= Q(team_id=q[0].team_1_id) | Q(team_id=q[0].team_2_id)
=======
	playername = models.ForeignKey('Player')
	match = models.ForeignKey('Match')
	points = models.IntegerField(default = 0)

	def __str__(self):
		return self.match.match_name





>>>>>>> d1c94c9d04de9168cc110551037b0345be010529

# Create your models here.
=======
>>>>>>> 63db62f4c73dc5f00ed00e4a89f79f9634d8944c
