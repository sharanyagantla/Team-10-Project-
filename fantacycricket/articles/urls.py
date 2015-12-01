from django.conf.urls import patterns, include,url

urlpatterns = patterns('',
	url(r'^all/', 'articles.views.article'),
	url(r'^get/(?P<article_id>\d+)/$' , 'articles.views.article')
)