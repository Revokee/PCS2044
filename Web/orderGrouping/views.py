from django import forms
from django.contrib import messages
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.template import Context, loader
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from orderGrouping.forms import *
from orderGrouping.models import *


# Funcao para cadastrar um pedido
def create_order(request):
	if request.method=='GET':
		create_order_form = CreateOrderForm()
		return render_to_response('novo_pedido.html', locals(), context_instance=RequestContext(request))
	else:
		create_order_form = CreateOrderForm(request.POST)
		if create_order_form.is_valid():
			new_order = create_order_form.save()
			messages.success(request, 'Pedido Cadastrado com sucesso')
			return HttpResponseRedirect('/pedidos/')
		messages.info(request, 'Formulario Nao OK')
		return render_to_response('novo_pedido.html', locals(), context_instance=RequestContext(request))

#Funcao para remover um pedido
def delete_order(request, order_id):
	order = Order.objects.get(pk=order_id)
	order.delete()
	messages.warning(request,'Pedido Deletado com sucesso')
	return HttpResponseRedirect('/pedidos/')


#Funcao para listar todos os pedidos
def index(request):
	orders = Order.objects.values()
	return render_to_response('pedidos.html', locals(), context_instance=RequestContext(request))