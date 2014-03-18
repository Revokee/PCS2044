from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.template import Context, loader
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse

# Views Estaticas!
def index(request):
	return render_to_response('index.html', locals(), context_instance=RequestContext(request))

def mapas(request):
	return render_to_response('mapas.html', locals(), context_instance=RequestContext(request))

def login(request):
	return render_to_response('login.html', locals(), context_instance=RequestContext(request))
