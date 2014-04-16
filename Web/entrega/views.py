#-*- coding: utf-8 -*-
from django import forms
from django.contrib import messages
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.views.decorators.csrf import csrf_exempt
from django.template import Context, loader
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from entrega.forms import *
from entrega.models import *
from pedido.models import *
from pygeocoder import Geocoder
import entrega.controller as Entrega

from django.contrib.auth import authenticate
from django.contrib.auth.decorators import permission_required, login_required

@csrf_exempt 
#Funcao de planejamento de entrega
def planejamento(request):
	pedidos = Pedido.objects.values()
	entregas = []
	addresses = []
	for pedido in pedidos:
		if pedido["entregue"]== False:
			entregas.append(pedido)
	if len(entregas) > 0:
		for entrega in entregas:
			addresses.append(entrega["rua"] + ", " + str(entrega["numero"]) + ", " + entrega["cidade"])
		#Entrega.EntregaController("Rua Apeninos, 990, Sao Paulo").bestRoute(addresses)["addresses"]
		print "Passou aqui - 1"
		rotas = Entrega.EntregaController("Rua Apeninos, 990, Sao Paulo").bestRoute(addresses)
		print "Passou aqui - 2"
		planejamento = []
		for address in rotas["addresses"]:
			results = Geocoder.geocode(address)
			latitude, longitude = results[0].coordinates
			planejamento.append((address, latitude, longitude))
		return render_to_response('planejamento.html', locals(), context_instance=RequestContext(request))
	else:
		messages.warning(request, 'Nao há entregas para serem feitas')
		return render_to_response('planejamento.html', locals(), context_instance=RequestContext(request))
