from forms import *
from django import forms
from django.contrib import messages
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.template import Context, loader
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from rh.forms import *
from rh.models import *

#Funcao para criar um novo entregador
def create_funcionario(request):
	if request.method=='GET':
		create_funcionario_form = CreateFuncionarioForm()
		return render_to_response('novo_entregador.html', locals(), context_instance=RequestContext(request))
	else:
		create_funcionario_form = CreateFuncionarioForm(request.POST)
		if create_funcionario_form.is_valid():
			new_funcionario = create_funcionario_form.save()
			messages.success(request, 'Entregador Cadastrado com sucesso')
			return HttpResponseRedirect('/entregadores/')
		messages.info(request, 'Formulario Nao OK')
		return render_to_response('novo_entregador.html', locals(), context_instance=RequestContext(request))

#Funcao para editar a posicao de um entregador
def edit_funcionario(request, funcionario_id):
	funcionario = Funcionario.objects.get(id=funcionario_id)
	if request.method=='GET':
		edit_funcionario_form = EditFuncionarioForm(instance=funcionario)
		return render_to_response('editar_entregador.html', locals(),context_instance=RequestContext(request)) 
	elif request.method=='POST':
		edit_funcionario_form = EditFuncionarioForm(request.POST,instance=funcionario)
		if edit_funcionario_form.is_valid():
			edit_funcionario_form.save()
			messages.success(request,'Entregador atualizado com sucesso')
			return HttpResponseRedirect('/entregadores/')
		else:
			messages.warning(request, 'Formulario Invalido')
			return render_to_response('editar_entregador.html', locals(),context_instance=RequestContext(request)) 


#Funcao para listar todos os entregadores
def index(request):
	funcionarios = Funcionario.objects.values()
	return render_to_response('entregadores.html', locals(), context_instance=RequestContext(request))

#Funcao para localizar um entregador no mapa
def funcionario_detail(request, Funcionario_id):
	funcionario = Funcionario.objects.get(id=funcionario_id)
	return render_to_response('mapas.html', locals(),context_instance=RequestContext(request))

#Funcao para remover um entregador
def delete_funcionario(request, funcionario_id):
	funcionario = Funcionario.objects.get(pk=funcionario_id)
	funcionario.delete()
	messages.warning(request,'Entregador Deletado com sucesso')
	return HttpResponseRedirect('/entregadores/')# Create your views here.
