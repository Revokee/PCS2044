from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from rh.models import Funcionario
from rh.models import Cargo, Contrato, Ferias, Licencas, Historico_Pagamentos
from django.core.urlresolvers import reverse_lazy

# CRUD funcionario
class FuncionarioList(ListView):
    model = Funcionario
    template_name = 'funcionarios/funcionarios_list.html'
    context_object_name = 'lista_funcionarios'
    success_url = reverse_lazy('funcionarios_list')

class FuncionarioCreate(CreateView):
    model = Funcionario
    template_name = 'funcionarios/funcionarios_form.html'
    fields = ['nome','sexo','endereco','telefone', 'cpf']
    success_url = reverse_lazy('funcionarios_list')

class FuncionarioUpdate(UpdateView):
    model = Funcionario
    template_name = 'funcionarios/funcionarios_form.html'
    fields = ['nome', 'cpf', 'endereco','telefone']
    success_url = reverse_lazy('funcionarios_list')

class FuncionarioDelete(DeleteView):
    model = Funcionario
    template_name = 'funcionarios/funcionarios_display.html'
    success_url = reverse_lazy('funcionarios_list')

class FuncionarioDetail(DetailView):
    model = Funcionario
    template_name = 'funcionarios/funcionarios_display.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(FuncionarioDetail, self).get_context_data(**kwargs)
        # Add in flag to indicate DetailView
        context['is_detail'] = True 
        return context  

# CRUD cargo
class CargoList(ListView):
    model = Cargo
    template_name = 'cargos/cargos_list.html'
    context_object_name = 'lista_cargos'
    success_url = reverse_lazy('cargos_list')

class CargoCreate(CreateView):
    model = Cargo
    template_name = 'cargos/cargos_form.html'
    fields = ['nome_cargo','nivel','salario']
    success_url = reverse_lazy('cargos_list')

class CargoUpdate(UpdateView):
    model = Cargo
    template_name = 'cargos/cargos_form.html'
    fields = ['nome_cargo','nivel','salario']
    success_url = reverse_lazy('cargos_list')

class CargoDelete(DeleteView):
    model = Cargo
    template_name = 'cargos/cargos_display.html'
    success_url = reverse_lazy('cargos_list')

class CargoDetail(DetailView):
    model = Cargo
    template_name = 'cargos/cargos_display.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(CargoDetail, self).get_context_data(**kwargs)
        # Add in flag to indicate DetailView
        context['is_detail'] = True 
        return context

# CRUD contrato
class ContratoList(ListView):
    model = Contrato
    template_name = 'contratos/contratos_list.html'
    context_object_name = 'lista_contratos'
    success_url = reverse_lazy('contratos_list')

class ContratoCreate(CreateView):
    model = Contrato
    template_name = 'contratos/contratos_form.html'
    fields = ['funcionario','cargo','data_contratacao','turno',
    'nome_contratante','observacoes','status_contrato',
    'data_demissao','motivo_demissao']
    success_url = reverse_lazy('contratos_list')

class ContratoUpdate(UpdateView):
    model = Contrato
    template_name = 'contratos/contratos_form.html'
    fields = ['funcionario','cargo','data_contratacao','turno',
    'nome_contratante','observacoes','status_contrato',
    'data_demissao','motivo_demissao']
    success_url = reverse_lazy('contratos_list')

class ContratoDelete(DeleteView):
    model = Contrato
    template_name = 'contratos/contratos_display.html'
    success_url = reverse_lazy('contratos_list')

class ContratoDetail(DetailView):
    model = Contrato
    template_name = 'contratos/contratos_display.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ContratoDetail, self).get_context_data(**kwargs)
        # Add in flag to indicate DetailView
        context['is_detail'] = True 
        return context

# CRUD ferias
class FeriasList(ListView):
    model = Ferias
    template_name = 'ferias/ferias_list.html'
    context_object_name = 'lista_ferias'
    success_url = reverse_lazy('ferias_list')

class FeriasCreate(CreateView):
    model = Ferias
    template_name = 'ferias/ferias_form.html'
    fields = ['funcionario','ano','data_inicio_ferias', 'numero_dias']
    success_url = reverse_lazy('ferias_list')

class FeriasUpdate(UpdateView):
    model = Ferias
    template_name = 'ferias/ferias_form.html'
    fields = ['ano','data_inicio_ferias', 'numero_dias']
    success_url = reverse_lazy('ferias_list')

class FeriasDelete(DeleteView):
    model = Ferias
    template_name = 'ferias/ferias_display.html'
    success_url = reverse_lazy('ferias_list')

class FeriasDetail(DetailView):
    model = Ferias
    template_name = 'ferias/ferias_display.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(FeriasDetail, self).get_context_data(**kwargs)
        # Add in flag to indicate DetailView
        context['is_detail'] = True 
        return context

# CRUD licenca
class LicencasList(ListView):
    model = Licencas
    template_name = 'licencas/licencas_list.html'
    context_object_name = 'lista_licencas'
    success_url = reverse_lazy('licencas_list')

class LicencasCreate(CreateView):
    model = Licencas
    template_name = 'licencas/licencas_form.html'
    fields = ['funcionario','data_inicio_licenca','numero_dias', 'remunerado', 'motivo']
    success_url = reverse_lazy('licencas_list')

class LicencasUpdate(UpdateView):
    model = Licencas
    template_name = 'licencas/licencas_form.html'
    fields = ['data_inicio_licenca','numero_dias', 'remunerado', 'motivo']
    success_url = reverse_lazy('licencas_list')

class LicencasDelete(DeleteView): 
    model = Licencas
    template_name = 'licencas/licencas_display.html'
    success_url = reverse_lazy('licencas_list')

class LicencasDetail(DetailView):
    model = Licencas
    template_name = 'licencas/licencas_display.html'
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(LicencasDetail, self).get_context_data(**kwargs)
        # Add in flag to indicate DetailView
        context['is_detail'] = True 
        return context

# CRUD historico
class Historico_PagamentosList(ListView):
    model = Historico_Pagamentos
    template_name = 'historico_pagamentos_list.html'
    context_object_name = 'lista_historico_pagamentos'

# ***********************
# ** INDEX Inteligente **
# ***********************

def IndexInteligente(request):
    entradas = Entrada.objects.all()
    mes_atual = datetime.datetime.now().strftime("%m")

    entradas_do_mes = Entrada.objects.filter(data_entrada__month=mes_atual)
    soma_entradas = entradas_do_mes.annotate(soma_entradas=Sum('valor'))
    saidas_do_mes = Saida.objects.filter(data_saida__month=mes_atual)
    soma_saidas = saidas_do_mes.annotate(soma_saidas=Sum('valor'))
    saldo_do_mes = soma_entradas.filter(soma_entradas) - soma_saidas 

    Saida.objects.all().aggregate(Max('price'))
    saldo_do_mes.order_by('-data_saida').values('destino','valor').aggregate(Max('valor'))

    #def getGastoesDoMes():
    entradas_do_mes = Entrada.objects.filter(data_entrada__month=mes_atual)
    entradas_do_mes.values('origem','valor').order_by('-valor')[:5]
    #entradas_do_mes.order_by('-data_entrada').values('origem','valor').aggregate(Max('valor'))

    #def getClientesDoMes():
    saidas_do_mes = Saida.objects.filter(data_saida__month=mes_atual)
    #saidas_do_mes.order_by('-data_saida').values('destino','valor').aggregate(Max('valor'))

    render(request, 'indexfinanceiro.html', {"soma_entradas": soma_entradas, "soma_saidas": soma_saidas, "saldo_do_mes": saldo_do_mes})
