from django import forms
from django.contrib import messages
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.views.decorators.csrf import csrf_exempt
from django.template import Context, loader
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from pedido.forms import *
from pedido.models import *
from pygeocoder import Geocoder
import pedido.controller as Ordenar

from django.contrib.auth import authenticate
from django.contrib.auth.decorators import permission_required, login_required

# Funcao para cadastrar um pedido
@csrf_exempt 
def create_pedido(request):
	if request.method=='GET':
		create_order_form = CreateOrderForm()
		return render_to_response('novo_pedido.html', locals(), context_instance=RequestContext(request))
	else:
		create_order_form = CreateOrderForm(request.POST)
		if create_order_form.is_valid():
			new_pedido = create_order_form.save(commit=False)
			address = ''+create_order_form.cleaned_data['rua']+','+str(create_order_form.cleaned_data['numero'])+','+create_order_form.cleaned_data['cidade']
			results = Geocoder.geocode(address)
			latitude, longitude = results[0].coordinates
			new_pedido.latitude = latitude
			new_pedido.longitude = longitude
			new_pedido.entregue = False
			new_pedido.save()
			messages.success(request, 'Pedido Cadastrado com sucesso')
			return HttpResponseRedirect('/pedidos/')
		messages.info(request, 'Formulario Nao OK')
		return render_to_response('novo_pedido.html', locals(), context_instance=RequestContext(request))

#Funcao para remover um pedido
def delete_pedido(request, pedido_id):
	pedido = Order.objects.get(pk=pedido_id)
	pedido.delete()
	messages.warning(request,'Pedido Deletado com sucesso')
	return HttpResponseRedirect('/pedidos/')



#Funcao para listar todos os pedidos
def index(request):
	if request.user.is_authenticated():
		if request.user.has_perm('pedido.change_order'):
			pedidos = Order.objects.values()
			return render_to_response('pedidos.html', locals(), context_instance=RequestContext(request))
		else:
			return render_to_response('index.html', locals(), context_instance=RequestContext(request))
	else:
		return render_to_response('login.html', locals(), context_instance=RequestContext(request))


#Funcao de planejamento de pedidos
def planejamento(request):
	pedidos = Order.objects.values()
	addresses = [pedido["rua"] + ", " + str(pedido["numero"]) + ", " + pedido["cidade"] for pedido in pedidos]
	#Ordenar.OrderController("Rua Apeninos, 990, Sao Paulo").bestRoute(addresses)["addresses"]
	rotas = Ordenar.OrderController("Rua Apeninos, 990, Sao Paulo").bestRoute(addresses)
	planejamento = []
	for address in rotas["addresses"]:
		results = Geocoder.geocode(address)
		latitude, longitude = results[0].coordinates
		planejamento.append((address, latitude, longitude))
	return render_to_response('planejamento.html', locals(), context_instance=RequestContext(request))

#Funcao clustering de pedidos
def clustering(request):
	pedidos = Order.objects.values()
	latitudes = [pedido["latitude"] for pedido in pedidos]
	longitudes = [pedido["longitude"] for pedido in pedidos]
	clusters = Ordenar.OrderController("").clustering(latitudes,longitudes)
	return render_to_response('clustering.html', locals(), context_instance=RequestContext(request))
