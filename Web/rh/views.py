from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from rh.models import Funcionario
from rh.models import Cargo, Contrato, Ferias, Licencas, Historico_Pagamentos
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Max, Sum
import datetime

# CRUD funcionario
class FuncionarioUpdate(SuccessMessageMixin, UpdateView):
    model = Funcionario
    template_name = 'funcionarios/funcionarios_form.html'
    fields = ['nome', 'cpf', 'endereco','telefone']
    success_url = reverse_lazy('funcionarios_list')
    success_message = 'Funcionario editado com sucesso.'

class FuncionarioList(ListView):
    model = Funcionario
    template_name = 'funcionarios/funcionarios_list.html'
    context_object_name = 'lista_funcionarios'
    success_url = reverse_lazy('funcionarios_list')

class FuncionarioCreate(SuccessMessageMixin, CreateView):
    model = Funcionario
    template_name = 'funcionarios/funcionarios_form.html'
    fields = ['nome','sexo','endereco','telefone', 'cpf']
    success_url = reverse_lazy('funcionarios_list')
    success_message = 'Funcionario criado com sucesso.'

class FuncionarioDelete(DeleteView):
    model = Funcionario
    template_name = 'funcionarios/funcionarios_display.html'
    success_url = reverse_lazy('funcionarios_list')

def get(self, request, *args, **kwargs):
    self.object = self.get_object()
    context = self.get_context_data(object=self.object)

    messages.success(request, 'Funcionario removido com sucesso.')
    return self.render_to_response(context)

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

class CargoCreate(SuccessMessageMixin, CreateView):
    model = Cargo
    template_name = 'cargos/cargos_form.html'
    fields = ['nome_cargo','nivel','salario']
    success_url = reverse_lazy('cargos_list')
    success_message = 'Cargo criado com sucesso.'

class CargoUpdate(SuccessMessageMixin, UpdateView):
    model = Cargo
    template_name = 'cargos/cargos_form.html'
    fields = ['nome_cargo','nivel','salario']
    success_url = reverse_lazy('cargos_list')
    success_message = 'Cargo editado com sucesso.'

class CargoDelete(DeleteView):
    model = Cargo
    template_name = 'cargos/cargos_display.html'
    success_url = reverse_lazy('cargos_list')

def get(self, request, *args, **kwargs):
    self.object = self.get_object()
    context = self.get_context_data(object=self.object)

    messages.success(request, 'Cargo removido com sucesso.')
    return self.render_to_response(context)

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

class ContratoCreate(SuccessMessageMixin, CreateView):
    model = Contrato
    template_name = 'contratos/contratos_form.html'
    fields = ['funcionario','cargo','data_contratacao','turno',
    'nome_contratante','observacoes','status_contrato',
    'data_demissao','motivo_demissao']
    success_url = reverse_lazy('contratos_list')
    success_message = 'Contrato criado com sucesso.'

class ContratoUpdate(SuccessMessageMixin, UpdateView):
    model = Contrato
    template_name = 'contratos/contratos_form.html'
    fields = ['funcionario','cargo','data_contratacao','turno',
    'nome_contratante','observacoes','status_contrato',
    'data_demissao','motivo_demissao']
    success_url = reverse_lazy('contratos_list')
    success_message = 'Contrato editado com sucesso.'

class ContratoDelete(DeleteView):
    model = Contrato
    template_name = 'contratos/contratos_display.html'
    success_url = reverse_lazy('contratos_list')

def get(self, request, *args, **kwargs):
    self.object = self.get_object()
    context = self.get_context_data(object=self.object)

    messages.success(request, 'Contrato removido com sucesso.')
    return self.render_to_response(context)

class ContratoDetail(DetailView):
    model = Contrato
    template_name = 'contratos/contratos_display.html'

def get_context_data(self, **kwargs):
    # Call the base implementation first to get a context
    context = super(ContratoDetail, self).get_context_data(**kwargs)
    # Add in flag to indicate DetailView
    context['is_detail'] = True 
    return context

class ContratoUpdateParaDemissao(SuccessMessageMixin, UpdateView):
    model = Contrato
    template_name = 'contratos/contratos_demissao.html'
    fields = ['observacoes','status_contrato',
    'data_demissao','motivo_demissao']
    success_url = reverse_lazy('contratos_list')
    success_message = 'Contrato modificado com sucesso.'

# CRUD ferias
class FeriasList(ListView):
    model = Ferias
    template_name = 'ferias/ferias_list.html'
    context_object_name = 'lista_ferias'
    success_url = reverse_lazy('ferias_list')

class FeriasCreate(SuccessMessageMixin, CreateView):
    model = Ferias
    template_name = 'ferias/ferias_form.html'
    fields = ['funcionario','ano','data_inicio_ferias', 'numero_dias']
    success_url = reverse_lazy('ferias_list')
    success_message = 'Ferias criadas com sucesso.'

class FeriasUpdate(SuccessMessageMixin, UpdateView):
    model = Ferias
    template_name = 'ferias/ferias_form.html'
    fields = ['ano','data_inicio_ferias', 'numero_dias']
    success_url = reverse_lazy('ferias_list')
    success_message = 'Ferias editadas com sucesso.'

class FeriasDelete(DeleteView):
    model = Ferias
    template_name = 'ferias/ferias_display.html'
    success_url = reverse_lazy('ferias_list')

def get(self, request, *args, **kwargs):
    self.object = self.get_object()
    context = self.get_context_data(object=self.object)

    messages.success(request, 'Ferias removidas com sucesso.')
    return self.render_to_response(context)

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

class LicencasCreate(SuccessMessageMixin, CreateView):
    model = Licencas
    template_name = 'licencas/licencas_form.html'
    fields = ['funcionario','data_inicio_licenca','numero_dias', 'remunerado', 'motivo']
    success_url = reverse_lazy('licencas_list')
    success_message = 'Licenca criada com sucesso.'

class LicencasUpdate(SuccessMessageMixin, UpdateView):
    model = Licencas
    template_name = 'licencas/licencas_form.html'
    fields = ['data_inicio_licenca','numero_dias', 'remunerado', 'motivo']
    success_url = reverse_lazy('licencas_list')
    success_message = 'Licenca editada com sucesso.'

class LicencasDelete(DeleteView): 
    model = Licencas
    template_name = 'licencas/licencas_display.html'
    success_url = reverse_lazy('licencas_list')

def get(self, request, *args, **kwargs):
    self.object = self.get_object()
    context = self.get_context_data(object=self.object)

    messages.success(request, 'Licenca removida com sucesso.')
    return self.render_to_response(context)

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
# ** Folha Pagamento **
# ***********************
class FolhaPagamento(ListView):
    model = Funcionario
    template_name = 'folha_pagamento.html'
    context_object_name = 'lista_funcionarios'
    success_url = reverse_lazy('folha_pagamento')

def get_context_data(self, **kwargs):
    # Call the base implementation first to get a context
    context = super(FolhaPagamento, self).get_context_data(**kwargs)
    # Add in flag to indicate DetailView
    allFuncionarios = Funcionario.objects.all()
    funcionariosComContratoValido   = allFuncionarios.filter(contrato__status_contrato='VALIDO_OK')
    mes_atual = datetime.datetime.now().strftime("%m")
    licencasDoMes = Licencas.objects.filter(data_inicio_licenca__month=mes_atual)
    for func in funcionariosComContratoValido:
        licencaFunc = Licencas.objects.filter(funcionario=func)
        if licencaFunc.count() > 0:
            if licencaFunc[0].data_inicio_licenca.strftime("%m") == mes_atual and not licencaFunc[0].remunerado:
                func.contrato.cargo.salario = int(func.contrato.cargo.salario) - ((int(func.contrato.cargo.salario)/30)*licencaFunc[0].numero_dias)

    soma_salarios = funcionariosComContratoValido.aggregate(soma=Sum('contrato__cargo__salario'))
    context['soma_salarios'] = soma_salarios['soma'] 
    context['funcValido'] = funcionariosComContratoValido 
    return context
