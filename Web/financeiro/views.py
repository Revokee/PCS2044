from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.core.urlresolvers import reverse_lazy
from financeiro.models import Entrada, Saida, SaldoMes
from django.shortcuts import render


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
    
class EntradaCreate(CreateView):
	model = Entrada
	template_name = 'entrada/entrada_form.html'
	fields = ['valor','data_entrada','origem','descricao','responsavel','forma_pagamento']
	success_url = reverse_lazy('entrada_list')

class EntradaUpdate(UpdateView):
	model = Entrada
	template_name = 'entrada/entrada_form.html'
	fields = ['valor','data_entrada','origem','descricao','responsavel','forma_pagamento']
	success_url = reverse_lazy('entrada_list')

class EntradaDelete(DeleteView):
	model = Entrada
	template_name = 'entrada/entrada_display.html'
	success_url = reverse_lazy('entrada_list')

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

class SaidaCreate(CreateView):
	model = Saida
	template_name = 'saida/saida_form.html'
	fields = ['valor','data_saida','destino','descricao','responsavel']
	success_url = reverse_lazy('saida_list')

class SaidaUpdate(UpdateView):
	model = Saida
	template_name = 'saida/saida_form.html'
	fields = ['valor','data_saida','destino','descricao','responsavel']
	success_url = reverse_lazy('saida_list')

class SaidaDelete(DeleteView):
	model = Saida
	template_name = 'saida/saida_display.html'
	success_url = reverse_lazy('saida_list')

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
	mes_atual = datetime.datetime.now().strftime("%m")

	entradas_do_mes = Entrada.objects.filter(data_entrada__month=mes_atual)
	soma_entradas = entradas_do_mes.aggregate(soma=Sum('valor'))
	soma_entradas = soma_entradas['soma']
	saidas_do_mes = Saida.objects.filter(data_saida__month=mes_atual)
	soma_saidas = saidas_do_mes.aggregate(soma=Sum('valor'))
	soma_saidas = soma_saidas['soma']
	saldo_do_mes = soma_entradas - soma_saidas

	#Saida.objects.all().aggregate(Max('valor'))
	#saldo_do_mes.order_by('-data_saida').values('destino','valor').aggregate(Max('valor'))

	#def getGastoesDoMes():
	#entradas_do_mes = Entrada.objects.filter(data_entrada__month=mes_atual)
	#entradas_do_mes.values('origem','valor').order_by('-valor')[:5]
	#entradas_do_mes.order_by('-data_entrada').values('origem','valor').aggregate(Max('valor'))

	#def getClientesDoMes():
	#saidas_do_mes = Saida.objects.filter(data_saida__month=mes_atual)
	saidas_do_mes.order_by('-data_saida').values('destino','valor').aggregate(Max('valor'))

	return render(request, 'index_financeiro.html', {"soma_entradas": soma_entradas, "soma_saidas": soma_saidas, "saldo_do_mes": saldo_do_mes})
