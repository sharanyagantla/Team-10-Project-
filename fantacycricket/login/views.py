
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib import auth
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from forms import MyRegistrationForm
from playy.models import Match, Team , Player  , UserProfile , AsignPoints
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render ,redirect
from django.core.urlresolvers import reverse


def login(request):
	c= {}
	c.update(csrf(request))
	q = Match.objects.all()
	# return render_to_response('login.html' , {c , 'match_name': q[0].match_name }  )
	t = loader.get_template('login.html')
	r = RequestContext(request, {'match_name': q  , 'user_names' : User.objects.all()[:5]} )
	return HttpResponse(t.render(r), content_type=c)


def auth_view(request):
	username = request.POST.get('username' , '')
	password = request.POST.get('password' , '')
	user = auth.authenticate(username=username , password = password)

	if user is not None :
		auth.login(request, user)
		return HttpResponseRedirect('/accounts/loggedin/')
	else :
		return HttpResponseRedirect('/accounts/invalid/')
		
		

def invalied_login(request):
	return render_to_response('invalied_login.html')


def loggedin(request):
	q = Match.objects.all()
	return render_to_response('loggedin.html' , {'full_name' : request.user.username , 'matchs_name' :q})

def logout(request):
	auth.logout(request)
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
	template = loader.get_template('select_team.html')
	c = {p}
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
			p1_points = assignpts.get(playername_id = p1id).points
			p2_points = assignpts.get(playername_id = p2id).points
			p3_points = assignpts.get(playername_id = p3id).points
			p4_points = assignpts.get(playername_id = p4id).points
			p5_points = assignpts.get(playername_id = p5id).points
			total_points = p1_points + p2_points + p3_points + p4_points + p5_points
			r = RequestContext(request, {'full_name' : request.user.username ,
            'match_name' : m.get(id = pk) , 'Team_1_name' : t.get(id = m.get(id = pk).team_1_id) ,
            'Team_2_name' : t.get(id = m.get(id = pk).team_2_id) , 
            'Team_1_players' : p.filter(team_id = m.get(id = pk).team_1_id) , 
            'Team_2_players' : p.filter(team_id = m.get(id = pk).team_2_id) ,
            'sel_player1' : all_sel_players.player_1 ,
            'p1_points' : p1_points,
            'p2_points' : p2_points,
            'p3_points' : p3_points,
            'p4_points' : p4_points,
            'p5_points' : p5_points,
            'sel_player2' : all_sel_players.player_2 ,
            'sel_player3' : all_sel_players.player_3 ,
            'sel_player4' : all_sel_players.player_4 ,
            'sel_player5' : all_sel_players.player_5 , 
            'tot_points' : total_points, 'key': pk, }  )	
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
            'sel_player2' : all_sel_players.player_2 ,
            'sel_player3' : all_sel_players.player_3 ,
            'sel_player4' : all_sel_players.player_4 ,
            'sel_player5' : all_sel_players.player_5 , 'key': pk }  )
			return HttpResponse(template.render(r3), content_type=c)
	except UserProfile.DoesNotExist :
		r2  = RequestContext(request, {'full_name' : request.user.username ,
            'match_name' : m.get(id = pk) , 'Team_1_name' : t.get(id = m.get(id = pk).team_1_id) ,
            'Team_2_name' : t.get(id = m.get(id = pk).team_2_id) , 
            'Team_1_players' : p.filter(team_id = m.get(id = pk).team_1_id) , 
            'Team_2_players' : p.filter(team_id = m.get(id = pk).team_2_id) , 'key' : pk } )
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
			,player_5_id= selected_choices[4] )
		except IndexError:
			return HttpResponseRedirect(reverse('selectTeam', args=(pk,)))
	except UserProfile.DoesNotExist :
		try :
			UserProfile.objects.create(user_id = request.user.id , match_id = pk ,
			player_1_id = selected_choices[0]  , player_2_id= selected_choices[1]  
			, player_3_id= selected_choices[2] , player_4_id= selected_choices[3] 
			,player_5_id= selected_choices[4] )
		except IndexError:
			return HttpResponseRedirect(reverse('selectTeam', args=(pk,)))
	return HttpResponseRedirect(reverse('selectTeam', args=(pk,)))

def index(request):
    return render_to_response('homepage.html', context_instance=RequestContext(request))



