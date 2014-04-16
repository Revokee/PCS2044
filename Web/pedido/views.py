#-*- coding: utf-8 -*-
from django import forms
from django.contrib import messages
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.views.decorators.csrf import csrf_exempt
from django.template import Context, loader
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from pedido.forms import *
from pedido.models import *
from entrega.models import *
from pygeocoder import Geocoder

from django.contrib.auth import authenticate
from django.contrib.auth.decorators import permission_required, login_required

def _parse_address(form):
	return form.cleaned_data['rua'] + ',' + unicode(form.cleaned_data['numero']) + ',' + form.cleaned_data['cidade']

# Funcao para cadastrar uma entrega
@csrf_exempt 
def novo(request):
	if request.user.is_authenticated():
		if request.user.has_perm('pedido.create_order'):
			if request.method=='GET':
				form = PedidoForm()
				return render_to_response('novo_pedido.html', locals(), context_instance=RequestContext(request))
			else:
				form = PedidoForm(request.POST)
				if form.is_valid():
					address = _parse_address(form)
					results = Geocoder.geocode(address)
					latitude, longitude = results[0].coordinates
					pedido = form.save(commit=False)
					pedido.latitude = latitude
					pedido.longitude = longitude
					pedido.entregue = False
					pedido.pago = False
					#pedido.Entrega = Entrega.objects.get(pk=0)
					pedido.save()
					messages.success(request, 'Pedido Cadastrado com sucesso')
					return HttpResponseRedirect('/pedido/')
				else:	
					messages.info(request, 'Formulario Nao OK')
					return render_to_response(request.path, locals(), context_instance=RequestContext(request))
		else:
			message.error(request, "Usuário desabilitado")
			return render_to_response('index.html', locals(), context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/login?next=' + request.path)
		#return render_to_response('login.html?next="' + request.path + '"', locals(), context_instance=RequestContext(request))

#Funcao para remover um pedido
def deletar(request, pedido_id):
	pedido = Pedido.objects.get(pk=pedido_id)
	if request.user.has_perm('pedido.delete_order'):
		pedido.delete()
		messages.warning(request,'Pedido Deletado com sucesso')
		return HttpResponseRedirect('/pedido/')
	else:
		message.error(request, "Usuário desabilitado")

def fechar(request, pedido_id):
	pedido = Pedido.objects.get(pk=pedido_id)
	return HttpResponseRedirect('/pedido/')

def pagar(request, pedido_id):
	pedido = Pedido.objects.get(pk=pedido_id)
	return HttpResponseRedirect('/pedido/')

#Funcao para listar todos os pedidos
def index(request):
	if request.user.is_authenticated():
		if request.user.has_perm('pedido.change_order'):
			pedidos = Pedido.objects.values().order_by('-id')
			return render_to_response('pedidos.html', locals(), context_instance=RequestContext(request))
		else:
			message.error(request, "Usuário desabilitado")
			return render_to_response('index.html', locals(), context_instance=RequestContext(request))
	else:
		return render_to_response('login.html', locals(), context_instance=RequestContext(request))
	pedidos = Order.objects.values()
	latitudes = [pedido["latitude"] for pedido in pedidos]
	longitudes = [pedido["longitude"] for pedido in pedidos]
	clusters = Ordenar.OrderController("").clustering(latitudes,longitudes)
	return render_to_response('clustering.html', locals(), context_instance=RequestContext(request))