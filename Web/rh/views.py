# -*- coding: utf-8 -*-
from forms import *
from django import forms
from django.views.generic import ListView, CreateView, UpdateView
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
		return render_to_response('novo_funcionario.html', locals(), context_instance=RequestContext(request))
	else:
		create_funcionario_form = CreateFuncionarioForm(request.POST)
		if create_funcionario_form.is_valid():
			new_funcionario = create_funcionario_form.save(commit=False)
			#Turnaround para nao ter q trabalhar com modelos relacionados
			new_funcionario.endereco_id = 1
			new_funcionario.pizzaria_id = 1
			new_funcionario.contrato_id_id = 1
			new_funcionario.save() 
			messages.success(request, 'Entregador Cadastrado com sucesso')
			return HttpResponseRedirect('/funcionarios/')
		messages.info(request, 'Formulário Não OK')
		return render_to_response('novo_funcionario.html', locals(), context_instance=RequestContext(request))

#Funcao para editar a posicao de um entregador
def edit_funcionario(request, funcionario_id):
	funcionario = Funcionario.objects.get(id=funcionario_id)
	if request.method=='GET':
		edit_funcionario_form = EditFuncionarioForm(instance=funcionario)
		return render_to_response('editar_funcionario.html', locals(),context_instance=RequestContext(request)) 
	elif request.method=='POST':
		edit_funcionario_form = EditFuncionarioForm(request.POST,instance=funcionario)
		if edit_funcionario_form.is_valid():
			edit_funcionario_form.save()
			messages.success(request,'Funcionário atualizado com sucesso')
			return HttpResponseRedirect('/funcionarios/')
		else:
			messages.warning(request, 'Formulário Inválido')
			return render_to_response('editar_funcionario.html', locals(),context_instance=RequestContext(request)) 


#Funcao para listar todos os entregadores
def index(request):
	funcionarios = Funcionario.objects.values()
	return render_to_response('funcionarios.html', locals(), context_instance=RequestContext(request))

#Funcao para localizar um entregador no mapa
def funcionario_detail(request, funcionario_id):
	funcionario = Funcionario.objects.get(id=funcionario_id)
	return render_to_response('mapas.html', locals(),context_instance=RequestContext(request))

#Funcao para remover um entregador
def delete_funcionario(request, funcionario_id):
	funcionario = Funcionario.objects.get(pk=funcionario_id)
	funcionario.delete()
	messages.warning(request,'Funcionário Deletado com sucesso')
	return HttpResponseRedirect('/funcionarios/')# Create your views here.


#Funcoes do Grupo do Rodrigo

# CRUD funcionario
class FuncionarioList(ListView):
    model = Funcionario
    template_name = 'funcionarios/funcionarios_list.html'
    context_object_name = 'lista_funcionarios'

class FuncionarioCreate(CreateView):
    model = Funcionario
    template_name = 'funcionarios/funcionarios_form.html'
    fields = ['nome','sexo','endereco','telefone']

class FuncionarioUpdate(UpdateView):
    model = Funcionario
    template_name = 'funcionarios/funcionarios_form.html'
    fields = ['endereco','telefone']

# CRUD cargo
class CargoList(ListView):
    model = Cargo
    template_name = 'cargos/cargos_list.html'
    context_object_name = 'lista_cargos'

class CargoCreate(CreateView):
    model = Cargo
    template_name = 'cargos/cargos_form.html'
    fields = ['nome_cargo','nivel','salario']

class CargoUpdate(UpdateView):
    model = Cargo
    template_name = 'cargos/cargos_form.html'
    fields = ['nome_cargo','nivel','salario']

# CRUD contrato
class ContratoList(ListView):
    model = Contrato
    template_name = 'contratos/contratos_list.html'
    context_object_name = 'lista_contratos'

class ContratoCreate(CreateView):
    model = Contrato
    template_name = 'contratos/contratos_form.html'
    fields = ['funcionario','cargo','data_contratacao','turno',
    'nome_contratante','observacoes','status_contrato',
    'data_demissao','motivo_demissao']

class ContratoUpdate(UpdateView):
    model = Contrato
    template_name = 'contratos/contratos_form.html'
    fields = ['funcionario','cargo','data_contratacao','turno',
    'nome_contratante','observacoes','status_contrato',
    'data_demissao','motivo_demissao']

# CRUD ferias
class FeriasList(ListView):
    model = Ferias
    template_name = 'ferias/ferias_list.html'
    context_object_name = 'lista_ferias'

class FeriasCreate(CreateView):
    model = Ferias
    template_name = 'ferias/ferias_form.html'
    fields = ['funcionario','ano','data_inicio_ferias', 'numero_dias']

class FeriasUpdate(UpdateView):
    model = Ferias
    template_name = 'ferias/ferias_form.html'
    fields = ['ano','data_inicio_ferias', 'numero_dias']

# CRUD licenca
class LicencasList(ListView):
    model = Licencas
    template_name = 'licencas/licencas_list.html'
    context_object_name = 'lista_licencas'

class LicencasCreate(CreateView):
    model = Licencas
    template_name = 'licencas/licencas_form.html'
    fields = ['funcionario','data_inicio_licenca','numero_dias', 'remunerado', 'motivo']

class LicencasUpdate(UpdateView):
    model = Licencas
    template_name = 'licencas/licencas_form.html'
    fields = ['data_inicio_licenca','numero_dias', 'remunerado', 'motivo']

# CRUD historico
class Historico_PagamentosList(ListView):
    model = Historico_Pagamentos
    template_name = 'historico_pagamentos_list.html'
    context_object_name = 'lista_historico_pagamentos'