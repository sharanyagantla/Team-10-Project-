from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from articles.models import Article

def hello(request) :
	name = 'Ram deekshith'
	html = "<html><body> Hi %s, how are you</body></html>" % name
	return HttpResponse(html)

def hello_template(request) :
	name = "ram"
	t = get_template('hello.html')
	html = t.render(Context({'name' : name}))
	return HttpResponse(html)

def simple_hello(request) :
	name = 'deekshith'
	return render_to_response('hello.html', {'name': name})

def home(request) :
	return render(request, "home.html")

def article(request):
	return render_to_response('articles.html',
		{ 'articles' : Article.objects.all() })

def articles(request, article_id=1):
	return render_to_response('article.html' ,
		{ 'article' : Article.objects.get(id=article_id) })