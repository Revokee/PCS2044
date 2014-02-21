from forms import *
from django import forms
from django.contrib import messages
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.template import Context, loader
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from deliverDetails.forms import *
from deliverDetails.models import *

#Funcao para criar um novo entregador
def create_deliver(request):
	if request.method=='GET':
		create_deliver_form = CreateDeliverForm()
		return render_to_response('novo_entregador.html', locals(), context_instance=RequestContext(request))
	else:
		create_deliver_form = CreateDeliverForm(request.POST)
		if create_deliver_form.is_valid():
			new_deliver = create_deliver_form.save()
			messages.success(request, 'Entregador Cadastrado com sucesso')
			return HttpResponseRedirect('/entregadores/')
		messages.info(request, 'Formulario Nao OK')
		return render_to_response('novo_entregador.html', locals(), context_instance=RequestContext(request))

#Funcao para editar a posicao de um entregador
def edit_deliver(request, deliver_id):
	deliver = Deliver.objects.get(id=deliver_id)
	if request.method=='GET':
		edit_deliver_form = EditDeliverForm(instance=deliver)
		return render_to_response('editar_entregador.html', locals(),context_instance=RequestContext(request)) 
	elif request.method=='POST':
		edit_deliver_form = EditDeliverForm(request.POST,instance=deliver)
		if edit_deliver_form.is_valid():
			edit_deliver_form.save()
			messages.success(request,'Entregador atualizado com sucesso')
			return HttpResponseRedirect('/entregadores/')
		else:
			messages.warning(request, 'Formulario Invalido')
			return render_to_response('editar_entregador.html', locals(),context_instance=RequestContext(request)) 


#Funcao para listar todos os entregadores
def index(request):
	delivers = Deliver.objects.values()
	return render_to_response('entregadores.html', locals(), context_instance=RequestContext(request))

#Funcao para localizar um entregador no mapa
def deliver_detail(request, deliver_id):
	deliver = Deliver.objects.get(id=deliver_id)
	return render_to_response('mapas.html', locals(),context_instance=RequestContext(request))

#Funcao para remover um entregador
def delete_deliver(request, deliver_id):
	deliver = Deliver.objects.get(pk=deliver_id)
	deliver.delete()
	messages.warning(request,'Entregador Deletado com sucesso')
	return HttpResponseRedirect('/entregadores/')