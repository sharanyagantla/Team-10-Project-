from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^accounts/login/', views.index, name='index'),
]