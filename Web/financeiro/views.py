from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from financeiro.models import Entrada, Saida, SaldoMes

# ******************
# ** CRUD Entrada **
# ******************

class EntradaList(ListView):
    model = Entrada
    template_name = 'entrada/entradas_list.html'
    context_object_name = 'lista_entradas'
    success_url = reverse_lazy('entrada_list')
    
class EntradaCreate(CreateView):
		model = Entrada
		template_name = 'entrada/entrada_form.html'
		fields = ['valor','data_entrada','origem','descricao','responsavel']
		success_url = reverse_lazy('entrada_list')

class EntradaUpdate(UpdateView):
		model = Entrada
		template_name = 'entrada/entrada_form.html'
		fields = ['valor','data_entrada','origem','descricao','responsavel']
		success_url = reverse_lazy('entrada_list')

class EntradaDelete(DeleteView):
		model = Entrada
		template_name = 'entrada/entrada_delete.html'
		success_url = reverse_lazy('entrada_list')

# ****************
# ** CRUD Saida **
# ****************

class SaidaList(ListView):
    model = Saida
    template_name = 'saida/saidas_list.html'
    context_object_name = 'lista_saidas'

# *******************
# ** CRUD SaldoMes **
# *******************

class SaldoMesList(ListView):
	model = SaldoMes
	template_name = 'saldomes/saldomes_list.html'
	context_object_name = 'lista_saldomes'