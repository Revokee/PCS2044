from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.template import Context, loader
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
#from entrega.models import *

# Views Estaticas!
def index(request):
#	pedidos = Order.objects.filter(entregue=False).count
	return render_to_response('index.html', locals(), context_instance=RequestContext(request))

def mapas(request):
	return render_to_response('mapas.html', locals(), context_instance=RequestContext(request))

def login_failed(request):
	return render_to_response('login.html', locals(), context_instance=RequestContext(request))

def login_account_disabled(request):
	return render_to_response('login.html', locals(), context_instance=RequestContext(request))

def lock(request):
	return render_to_response('lock.html', locals(), context_instance=RequestContext(request))
