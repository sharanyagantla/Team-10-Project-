
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.contrib import auth
from django.http import HttpResponse
from forms import MyRegistrationForm
from django.template import loader
from django.template import RequestContext
import datetime
from login.models import Match
from django.contrib import auth
from django.contrib.auth.models import User

def login(request):
	z= {}
	z.update(csrf(request))
	u = User.objects.all()
	q = Match.objects.all()
	t = loader.get_template('login.html')
	c = RequestContext(request, {'match_name': q})
	return HttpResponse(t.render(c), content_type=z)

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
	z= {}
	z.update(csrf(request))
	q = Match.objects.all()
	t = loader.get_template('loggedin.html')
	c = RequestContext(request, {'match_name': q })
	return HttpResponse(t.render(c), content_type=z)
	return render_to_response('loggedin.html' ,
		{'full_name' : request.user.username})

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

def hello_world(request):
    context = {}
    context['current_time'] = datetime.datetime.now()
    template = loader.get_template('loggedin.html')
    data = RequestContext(request, context)
    return HttpResponse(template.render(data))	

