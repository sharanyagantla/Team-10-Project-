# from django.shortcuts import render_to_response
# from django.http import HttpResponseRedirect
# from django.core.context_processors import csrf
# from django.contrib import auth
# # from django.contrib.auth.forms import UserCreationForm
# # from django.contrib.auth.models import User
# from django.http import HttpResponse
# from forms import MyRegistrationForm

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

