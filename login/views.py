
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib import auth
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from forms import MyRegistrationForm
from login.models import Match
from django.template import RequestContext, loader


def login(request):
	c= {}
	c.update(csrf(request))
	q = Match.objects.all()
	# return render_to_response('login.html' , {c , 'match_name': q[0].match_name }  )
	t = loader.get_template('login.html')
	r = RequestContext(request, {'match_name': q  , 'user_names' : User.objects.all()} )
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

	# def loggedin(request):
	# return render_to_response('loggedin.html' ,{'full_name' : request.user.username})

def loggedin(request):
	c= {}
	c.update(csrf(request))
	q = Match.objects.all()
	t = loader.get_template('loggedin.html')
	r = RequestContext(request, {'match_name': q , 'full_name' : request.user.username} )
	return HttpResponse(t.render(r), content_type=c)


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

def index(request):
    return render_to_response('homepage.html', context_instance=RequestContext(request))	