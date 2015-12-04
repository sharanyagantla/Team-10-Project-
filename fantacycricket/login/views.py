
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib import auth
# from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from forms import MyRegistrationForm
from playy.models import Match, Team , Player  , UserProfile , AsignPoints , Points
from django.contrib.auth.models import User
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render ,redirect
from django.core.urlresolvers import reverse
from datetime import datetime 
from django.utils import timezone

def gamerules(request):
	return render_to_response('gamerules.html')

def index(request):
    return render_to_response('homepage.html', context_instance=RequestContext(request))

def login(request):
	c= {}
	c.update(csrf(request))
	q = Match.objects.all()
	t = loader.get_template('login.html')
	r = RequestContext(request, {'match_name': q  , 'user_names' : Points.objects.all().extra(order_by = ['-full_points'])[:5]} )
	return HttpResponse(t.render(r), content_type=c)


def auth_view(request):
	if request.method == 'POST':
		email = request.POST.get('email' ,False)
		username = request.POST.get('username' , '')
		password = request.POST.get('password' , '')
		user = auth.authenticate(username=username , password = password)
		if "username" not in request.session or (username == request.session["username"]) :
			if user is not None :
				auth.login(request, user)
				request.session["username"] = username
				return HttpResponseRedirect('/accounts/loggedin/')
			else :
				return HttpResponseRedirect('/accounts/invalid/')
		else :
			return HttpResponse("user already logged in")
		
		

def invalied_login(request):
	return render_to_response('invalied_login.html')


def loggedin(request):
	if request.user.id is not None :
		q = Match.objects.all()
		try:
			return render_to_response('loggedin.html' , {'full_name' : request.user.username , 'matchs_name' :q , 
	     'curr_points' :  Points.objects.all().get(user_id = request.user.id).full_points })
		except :
			return render_to_response('loggedin.html' , {'full_name' : request.user.username , 'matchs_name' :q ,'curr_points' : 0})
	else :
		return login(request)


def logout(request):
	auth.logout(request)
	if "username" in request.session:
		del request.session["username"]
	return render_to_response('logout.html')

def register_user(request):
	if request.method == 'POST' :
		form = MyRegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/accounts/register_sucesss/')
		else:
			return render_to_response('registerpasswordsmatch_alert.html')
			
	args = {}
	args.update(csrf(request))

	args['form'] = MyRegistrationForm()
	
	return render_to_response('register.html' ,args)

def register_sucesss(request):
	return render_to_response('register_sucesss.html')


def select_team(request , pk):
	m = Match.objects.all()
	p = Player.objects.all()
	a= AsignPoints.objects.all()
	t = Team.objects.all()
	userid = request.user.id
	today = timezone.now()
	if(m.get(id = pk).pub_date < today) :
		flag = 1
	else :
		flag = 0
	if(flag == 1):
		lbp = UserProfile.objects.all().filter(match_id = pk).extra(order_by = ['-total_points'])[:5]
	else:
		lbp = []
	leader_length = len(lbp)
	if len(lbp) >=1 :
		lbp1 = lbp[0]
	else :
		lbp1 = None
	if len(lbp) >=2 :
		lbp2 = lbp[1]
	else :
		lbp2 = None
	if len(lbp) >=3 :
		lbp3 = lbp[2]
	else :
		lbp3 = None
	if len(lbp) >=4 :
		lbp4 = lbp[3]
	else :
		lbp4 = None
	if len(lbp) >=5 :
		lbp5 = lbp[4]
	else :
		lbp5 = None
	template = loader.get_template('select_team.html')
	c = {p}
	if request.user.is_superuser: 
		template3 = loader.get_template('assignpoints.html')
		r5 = RequestContext(request, {'Team_1_players' : p.filter(team_id = m.get(id = pk).team_1_id) ,
		'Team_2_players' : p.filter(team_id = m.get(id = pk).team_2_id), 'key' : pk,  'test' : flag , 'lbp1' : lbp1 
		, 'lbp2' : lbp2 ,'lbp3' : lbp3 ,'lbp4' : lbp4,'lbp5' : lbp5 , 'leader_length' :leader_length})
		return HttpResponse(template3.render(r5), content_type=c)
	try :
		u = UserProfile.objects.all()
		all_sel_players = u.filter(user_id = userid).get(match_id = pk)
		try :
			assignpts = AsignPoints.objects.all().filter(match_id = pk)
			p1id = all_sel_players.player_1_id
			p2id = all_sel_players.player_2_id
			p3id = all_sel_players.player_3_id
			p4id = all_sel_players.player_4_id
			p5id = all_sel_players.player_5_id
			ppid = all_sel_players.power_player_id
			p1_points = assignpts.get(playername_id = p1id).points
			p2_points = assignpts.get(playername_id = p2id).points
			p3_points = assignpts.get(playername_id = p3id).points
			p4_points = assignpts.get(playername_id = p4id).points
			p5_points = assignpts.get(playername_id = p5id).points
			pp_points = assignpts.get(playername_id = ppid).points
			total_points = p1_points + p2_points + p3_points + p4_points + p5_points + pp_points
			r = RequestContext(request, {'full_name' : request.user.username ,
            'match_name' : m.get(id = pk) , 'Team_1_name' : t.get(id = m.get(id = pk).team_1_id) ,
            'Team_2_name' : t.get(id = m.get(id = pk).team_2_id) , 
            'Team_1_players' : p.filter(team_id = m.get(id = pk).team_1_id) , 
            'Team_2_players' : p.filter(team_id = m.get(id = pk).team_2_id) ,
            'p1_points' : p1_points,
            'p2_points' : p2_points,
            'p3_points' : p3_points,
            'p4_points' : p4_points,
            'p5_points' : p5_points,
            'pp_points' : pp_points,
            'sel_player1' : all_sel_players.player_1 ,
            'sel_player2' : all_sel_players.player_2 ,
            'sel_player3' : all_sel_players.player_3 ,
            'sel_player4' : all_sel_players.player_4 ,
            'sel_player5' : all_sel_players.player_5 , 
            'sel_pp' : all_sel_players.power_player,
            'tot_points' : total_points, 'key': pk,  'test' : flag  ,  'lbp1' : lbp1 
		, 'lbp2' : lbp2 ,'lbp3' : lbp3 ,'lbp4' : lbp4,'lbp5' : lbp5 , 'leader_length' :leader_length })	
			return HttpResponse(template.render(r), content_type=c)
		except AsignPoints.DoesNotExist :
			r3 = RequestContext(request, {'full_name' : request.user.username ,
            'match_name' : m.get(id = pk) , 'Team_1_name' : t.get(id = m.get(id = pk).team_1_id) ,
            'Team_2_name' : t.get(id = m.get(id = pk).team_2_id) , 
            'Team_1_players' : p.filter(team_id = m.get(id = pk).team_1_id) , 
            'Team_2_players' : p.filter(team_id = m.get(id = pk).team_2_id) ,
            'sel_player1' : all_sel_players.player_1 ,
            'p1_points' : 0,
            'p2_points' : 0,
            'p3_points' : 0,
            'p4_points' : 0,
            'p5_points' : 0,
            'pp_points' : 0,
            'sel_player2' : all_sel_players.player_2 ,
            'sel_player3' : all_sel_players.player_3 ,
            'sel_player4' : all_sel_players.player_4 ,
            'sel_player5' : all_sel_players.player_5 ,
            'sel_pp' : all_sel_players.power_player, 'key': pk ,'test' : flag }  )
			return HttpResponse(template.render(r3), content_type=c)
	except UserProfile.DoesNotExist :
		r2  = RequestContext(request, {'full_name' : request.user.username ,
            'match_name' : m.get(id = pk) , 'Team_1_name' : t.get(id = m.get(id = pk).team_1_id) ,
            'Team_2_name' : t.get(id = m.get(id = pk).team_2_id) , 
            'Team_1_players' : p.filter(team_id = m.get(id = pk).team_1_id) , 
            'Team_2_players' : p.filter(team_id = m.get(id = pk).team_2_id) , 'key' : pk ,'test' : flag , 'lbp1' : lbp1 
		, 'lbp2' : lbp2 ,'lbp3' : lbp3 ,'lbp4' : lbp4,'lbp5' : lbp5 , 'leader_length' :leader_length} )
		return HttpResponse(template.render(r2), content_type=c)


def vote(request , pk):
	p = Player.objects.all()
	selected_choices  = request.POST.getlist('playerr')
	try:
		try:
			obj = UserProfile.objects.get(user_id = request.user.id , match_id = pk )
			UserProfile.objects.filter(user_id = request.user.id).filter( match_id = pk).update(user_id = request.user.id , match_id = pk ,
			player_1_id = selected_choices[0]  , player_2_id= selected_choices[1]  
			, player_3_id= selected_choices[2] , player_4_id= selected_choices[3] 
			,player_5_id= selected_choices[4] , power_player_id =  selected_choices[0] )
		except IndexError:
			return HttpResponseRedirect(reverse('selectTeam', args=(pk,)))
	except UserProfile.DoesNotExist :
		try :
			UserProfile.objects.create(user_id = request.user.id , match_id = pk ,
			player_1_id = selected_choices[0]  , player_2_id= selected_choices[1]  
			, player_3_id= selected_choices[2] , player_4_id= selected_choices[3] 
			,player_5_id= selected_choices[4]  , power_player_id =  selected_choices[0] )
		except IndexError:
			return HttpResponseRedirect(reverse('selectTeam', args=(pk,)))
	return render(request , "selectPowerplayer.html" , {'players' : UserProfile.objects.get(user_id = request.user.id , match_id = pk ) , 'matchid':pk})

def powerplayer(request , pk):
	try:
		if request.method=='POST':
			choice=request.POST['pplayer']
		UserProfile.objects.filter(user_id = request.user.id).filter(match_id = pk ).update(power_player_id = choice)
	except :
		return render(request , "selectPowerplayer.html" , {'players' : UserProfile.objects.get(user_id = request.user.id , match_id = pk ) , 'matchid':pk})
	return HttpResponseRedirect('/accounts/loggedin/')

def savepoints(request , pk) :
	all_points = request.POST.getlist('playerPoints')
	playerid = request.POST.getlist('playerid')
	for i in xrange(len(all_points)):
		try :
			AsignPoints.objects.all().filter(match_id = pk).get(playername_id = playerid[i])
			AsignPoints.objects.all().filter(match_id = pk).filter(playername_id = playerid[i]).update( points = all_points[i])
		except:
			try:
				AsignPoints.objects.create(match_id = pk , playername_id = playerid[i] , points = all_points[i])
			except:
				continue
	up = UserProfile.objects.all()
	u = User.objects.all()
	assignpts = AsignPoints.objects.all().filter(match_id = pk)
	for uid in u:
		try :
			all_sel_players = up.filter(user_id = uid.id).get(match_id = pk)
			p1id = all_sel_players.player_1_id
			p2id = all_sel_players.player_2_id
			p3id = all_sel_players.player_3_id
			p4id = all_sel_players.player_4_id
			p5id = all_sel_players.player_5_id
			ppid = all_sel_players.power_player_id
			p1_points = assignpts.get(playername_id = p1id).points
			p2_points = assignpts.get(playername_id = p2id).points
			p3_points = assignpts.get(playername_id = p3id).points
			p4_points = assignpts.get(playername_id = p4id).points
			p5_points = assignpts.get(playername_id = p5id).points
			pp_points = assignpts.get(playername_id = ppid).points
			total_points = p1_points + p2_points + p3_points + p4_points + p5_points + pp_points
			up.filter(user_id = uid.id).filter(match_id = pk).update(total_points = total_points)
		except :
			continue
	return HttpResponse("sucess")

def finalpoints(request , pk) :
	all_points = request.POST.getlist('playerPointsf')
	playerid = request.POST.getlist('playeridf')
	for i in xrange(len(all_points)):
		try :
			AsignPoints.objects.all().filter(match_id = pk).get(playername_id = playerid[i])
			AsignPoints.objects.all().filter(match_id = pk).filter(playername_id = playerid[i]).update( points = all_points[i])
		except:
			AsignPoints.objects.create(match_id = pk , playername_id = playerid[i] , points = all_points[i])
	up = UserProfile.objects.all()
	u = User.objects.all()
	assignpts = AsignPoints.objects.all().filter(match_id = pk)
	for uid in u:
		try :
			all_sel_players = up.filter(user_id = uid.id).get(match_id = pk)
			p1id = all_sel_players.player_1_id
			p2id = all_sel_players.player_2_id
			p3id = all_sel_players.player_3_id
			p4id = all_sel_players.player_4_id
			p5id = all_sel_players.player_5_id
			ppid = all_sel_players.power_player_id
			p1_points = assignpts.get(playername_id = p1id).points
			p2_points = assignpts.get(playername_id = p2id).points
			p3_points = assignpts.get(playername_id = p3id).points
			p4_points = assignpts.get(playername_id = p4id).points
			p5_points = assignpts.get(playername_id = p5id).points
			pp_points = assignpts.get(playername_id = ppid).points
			total_points = p1_points + p2_points + p3_points + p4_points + p5_points + pp_points
			up.filter(user_id = uid.id).filter(match_id = pk).update(total_points = total_points)
			try :
				Points.objects.all().filter(user_id = uid.id ).update(full_points = total_points+Points.objects.all().get(user_id = uid.id).full_points )
			except :
				Points.objects.create( user_id = uid.id , full_points = total_points )
		except :
			continue
	return HttpResponse("sucess")



def userTeam(request , pk ,mid):
	players_list =  UserProfile.objects.all().get(id = pk)
	user_profile = AsignPoints.objects.all().filter(match_id = mid).get(playername_id = players_list.player_1_id)
	p1_points = AsignPoints.objects.all().filter(match_id = mid).get(playername_id = players_list.player_1_id).points
	p2_points = AsignPoints.objects.all().filter(match_id = mid).get(playername_id = players_list.player_2_id).points
	p3_points = AsignPoints.objects.all().filter(match_id = mid).get(playername_id = players_list.player_3_id).points
	p4_points = AsignPoints.objects.all().filter(match_id = mid).get(playername_id = players_list.player_4_id).points
	p5_points = AsignPoints.objects.all().filter(match_id = mid).get(playername_id = players_list.player_5_id).points
	pp_points = AsignPoints.objects.all().filter(match_id = mid).get(playername_id = players_list.power_player_id).points
	total = p1_points + p2_points + p3_points + p4_points + p5_points + pp_points
	return render_to_response('userTeam.html' , {'p1_points' : p1_points , 'p2_points' : p2_points , 'p3_points' : p3_points,
	'p4_points' : p4_points,'p5_points' : p5_points , 'pp_points' : pp_points , 'p1' : players_list.player_1 , 'p2' : players_list.player_2 ,
	'p3' : players_list.player_3 , 'p4' : players_list.player_4 , 'p5' : players_list.player_5 , 'pp' : players_list.power_player ,'total' :total , 'profile' :user_profile })

