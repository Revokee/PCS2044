from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.core.urlresolvers import reverse_lazy
from financeiro.models import Entrada, Saida, SaldoMes
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

import datetime
from django.db.models import Max, Sum

# ******************
# ** CRUD Entrada **
# ******************

class EntradaList(ListView):
    model = Entrada
    template_name = 'entrada/entradas_list.html'
    context_object_name = 'lista_entradas'
    success_url = reverse_lazy('entrada_list')

    def get_queryset(self):
    		return Entrada.objects.order_by('-data_entrada')
    
class EntradaCreate(SuccessMessageMixin, CreateView):
	model = Entrada
	template_name = 'entrada/entrada_form.html'
	fields = ['valor','data_entrada','origem','descricao','responsavel','forma_pagamento']
	success_url = reverse_lazy('entrada_list')
	success_message = "Entrada criada com sucesso."

class EntradaUpdate(SuccessMessageMixin, UpdateView):
	model = Entrada
	template_name = 'entrada/entrada_form.html'
	fields = ['valor','data_entrada','origem','descricao','responsavel','forma_pagamento']
	success_url = reverse_lazy('entrada_list')
	success_message = "Entrada editada com sucesso."

class EntradaDelete(DeleteView):
	model = Entrada
	template_name = 'entrada/entrada_display.html'
	success_url = reverse_lazy('entrada_list')

	def get(self, request, *args, **kwargs):
		self.object = self.get_object()
		context = self.get_context_data(object=self.object)

		messages.success(request, 'Entrada removida com sucesso.')
		return self.render_to_response(context)

class EntradaDetail(DetailView):
	model = Entrada
	template_name = 'entrada/entrada_display.html'
	
	def get_context_data(self, **kwargs):
	    # Call the base implementation first to get a context
	    context = super(EntradaDetail, self).get_context_data(**kwargs)
	    # Add in flag to indicate DetailView
	    context['is_detail'] = True 
	    return context	

# ****************
# ** CRUD Saida **
# ****************

class SaidaList(ListView):
    model = Saida
    template_name = 'saida/saidas_list.html'
    context_object_name = 'lista_saidas'
    success_url = reverse_lazy('saida_list')

    def get_queryset(self):
    		return Saida.objects.order_by('-data_saida')

class SaidaCreate(SuccessMessageMixin, CreateView):
	model = Saida
	template_name = 'saida/saida_form.html'
	fields = ['valor','data_saida','destino','descricao','responsavel']
	success_url = reverse_lazy('saida_list')
	success_message = "Saida criada com sucesso."

class SaidaUpdate(SuccessMessageMixin, UpdateView):
	model = Saida
	template_name = 'saida/saida_form.html'
	fields = ['valor','data_saida','destino','descricao','responsavel']
	success_url = reverse_lazy('saida_list')
	success_message = "Saida editada com sucesso."

class SaidaDelete(DeleteView):
	model = Saida
	template_name = 'saida/saida_display.html'
	success_url = reverse_lazy('saida_list')
	
	def get(self, request, *args, **kwargs):
		self.object = self.get_object()
		context = self.get_context_data(object=self.object)

		messages.success(request, 'Saida removida com sucesso.')
		return self.render_to_response(context)

class SaidaDetail(DetailView):
	model = Saida
	template_name = 'saida/saida_display.html'
	
	def get_context_data(self, **kwargs):
	    # Call the base implementation first to get a context
	    context = super(SaidaDetail, self).get_context_data(**kwargs)
	    # Add in flag to indicate DetailView
	    context['is_detail'] = True 
	    return context

# *******************
# ** CRUD SaldoMes **
# *******************

class SaldoMesList(ListView):
	model = SaldoMes
	template_name = 'saldomes/saldomes_list.html'
	context_object_name = 'lista_saldomes'

# ***********************
# ** INDEX Inteligente **
# ***********************

def IndexInteligente(request):
	entradas = Entrada.objects.all()
	saidas = Saida.objects.all()
	mes_atual = datetime.datetime.now().strftime("%m")

	# ENTRADAS DO MES
	entradas_do_mes = Entrada.objects.filter(data_entrada__month=mes_atual)
	soma_entradas = entradas_do_mes.aggregate(soma=Sum('valor'))
	soma_entradas = soma_entradas['soma']
	if soma_entradas is None:
		soma_entradas = 0
	saidas_do_mes = Saida.objects.filter(data_saida__month=mes_atual)
	soma_saidas = saidas_do_mes.aggregate(soma=Sum('valor'))
	soma_saidas = soma_saidas['soma']
	if soma_saidas is None:
		soma_saidas = 0
	saldo_do_mes = soma_entradas - soma_saidas

	# MAIORES ENTRADAS DO MES
	entradas_por_origem = Entrada.objects.values('origem').annotate(soma=Sum('valor')).order_by('-soma')[:5]
	print entradas_por_origem

	# ULTIMAS ENTRADAS
	ultimas_entradas = entradas[:5]

	# ULTIMAS SAIDAS
	ultimas_saidas = saidas[:5]

	return render(request, 'index_financeiro.html', {
		"soma_entradas": soma_entradas,
		"soma_saidas": soma_saidas,
		"saldo_do_mes": saldo_do_mes,
		"entradas_por_origem": entradas_por_origem,
		"ultimas_entradas": ultimas_entradas,
		"ultimas_saidas": ultimas_saidas
		})
