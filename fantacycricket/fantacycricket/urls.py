"""fantacycricket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = patterns('' ,
	url(r'^admin/', include(admin.site.urls)),
	# url(r'^article/', include('articles.urls')),
    url(r'^$', 'login.views.index'),
    url(r'^accounts/homepage/', 'login.views.index'),
    url(r'^accounts/gamerules/', 'login.views.gamerules'),
    url(r'^accounts/login/', 'login.views.login'),
    url(r'^accounts/auth/' , 'login.views.auth_view'),
    url(r'^accounts/logout/' , 'login.views.logout'),
    url(r'^accounts/loggedin/', 'login.views.loggedin' , name='loggedin'),
    url(r'^accounts/invalid/' , 'login.views.invalied_login'),
    url(r'^accounts/register/' , 'login.views.register_user'),
    url(r'^accounts/register_sucesss/' , 'login.views.register_sucesss'),
    url(r'^accounts/select_team/(?P<pk>[0-9]+)/' , 'login.views.select_team' , name = "selectTeam"),
    url(r'^accounts/select_team/vote/(?P<pk>[0-9]+)/$', 'login.views.vote', name='vote'),
    url(r'^accounts/select_team/points/(?P<pk>[0-9]+)/$', 'login.views.savepoints', name='assignpoints'),
    url(r'^accounts/select_team/finalpoints/(?P<pk>[0-9]+)/$', 'login.views.finalpoints', name='assignpointsfinal'),
    url(r'^accounts/select_team/userTeam/(?P<pk>[0-9]+)/(?P<mid>[0-9]+)/$', 'login.views.userTeam', name='userTeam'),
    url(r'^accounts/select_team/powerplayer/(?P<pk>[0-9]+)$', 'login.views.powerplayer', name='powerplayer'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
