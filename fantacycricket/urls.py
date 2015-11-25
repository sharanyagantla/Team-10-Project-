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

# admin.autodiscover()
# urlpatterns = [
#     url(r'^admin/', include(admin.site.urls)),
#     url(r'^hello/', 'articles.views.hello'),
#     url(r'^hello_template/' , 'articles.views.hello_template'),
#     url(r'^simple_hello/' , 'articles.views.simple_hello'),
#     url(r'^', 'articles.views.home'),
# ]


urlpatterns = patterns('' ,
	url(r'^admin/', include(admin.site.urls)),
	# url(r'^article/', include('articles.urls')),
    url(r'^accounts/login/', 'login.views.login'),
    url(r'^accounts/auth/' , 'login.views.auth_view'),
    url(r'^accounts/logout/' , 'login.views.logout'),
   # url(r'^accounts/loggedin/', 'login.views.loggedin'),
    url(r'^accounts/loggedin/', 'login.views.hello_world'),
    url(r'^accounts/invalid/' , 'login.views.invalied_login'),
    url(r'^accounts/register/' , 'login.views.register_user'),
    url(r'^accounts/register_sucesss/' , 'login.views.register_sucesss'),
)
