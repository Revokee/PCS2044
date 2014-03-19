# Create your views here.
from django import forms
from django.contrib import messages
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.views.decorators.csrf import csrf_exempt
from django.template import Context, loader
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse

from django.contrib.auth import authenticate, login as django_login

@csrf_exempt
def login(request):
        if request.method=='GET':
                return render_to_response('login.html', locals(), context_instance=RequestContext(request))
        else:
		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				django_login(request, user)
                		return render_to_response('index.html', locals(), context_instance=RequestContext(request))
				# Redirect to a success page.
			else:
                		return render_to_response('login_account_disabled.html', locals(), context_instance=RequestContext(request))
				# Return a 'disabled account' error message
		else:
                	return render_to_response('login_failed.html', locals(), context_instance=RequestContext(request))
			# Return an 'invalid login' error message.
