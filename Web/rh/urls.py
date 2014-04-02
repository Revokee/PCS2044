from django.conf.urls import patterns, include, url
from pizza5.rh.views import FuncionarioList, FuncionarioCreate, FuncionarioUpdate, CargoList, ContratoList, FeriasList, LicencasList, Historico_PagamentosList
from pizza5.rh.views import *
from django.views.generic import TemplateView

urlpatterns = patterns('',
	url(r'^$', TemplateView.as_view(template_name="../templates/index_rh.html"), name="index_rh"),
    url(r'^funcionarios/lista_funcionarios/$', FuncionarioList.as_view(), name='funcionarios_list') ,
    url(r'^funcionarios/cria_funcionario/$', FuncionarioCreate.as_view(), name='funcionario_create'),
    url(r'^funcionarios/edita_funcionario/(?P<pk>\d+)$', FuncionarioUpdate.as_view(), name='funcionario_update'),
    url(r'^funcionarios/remove_funcionario/(?P<pk>\d+)$', FuncionarioDelete.as_view(), name='funcionario_delete'),
    url(r'^funcionarios/detalha_funcionario/(?P<pk>\d+)$', FuncionarioDetail.as_view(), name='funcionario_detail'),

    url(r'^cargos/lista_cargos/$', CargoList.as_view(), name='cargos_list') ,
    url(r'^cargos/cria_cargo/$', CargoCreate.as_view(), name='cargo_create'),
    url(r'^cargos/edita_cargo/(?P<pk>\d+)$', CargoUpdate.as_view(), name='cargo_update'),
    url(r'^cargos/remove_cargo/(?P<pk>\d+)$', CargoDelete.as_view(), name='cargo_delete'),
    url(r'^cargos/detalha_cargo/(?P<pk>\d+)$', CargoDetail.as_view(), name='cargo_detail'),

    url(r'^contratos/lista_contratos/$', ContratoList.as_view(), name='contratos_list') ,
    url(r'^contratos/cria_contrato/$', ContratoCreate.as_view(), name='contrato_create'),
    url(r'^contratos/edita_contrato/(?P<pk>\d+)$', ContratoUpdate.as_view(), name='contrato_update'),
    url(r'^contratos/remove_contrato/(?P<pk>\d+)$', ContratoDelete.as_view(), name='contrato_delete'),
    url(r'^contratos/detalha_contrato/(?P<pk>\d+)$', ContratoDetail.as_view(), name='contrato_detail'),

    url(r'^ferias/lista_ferias/$', FeriasList.as_view(), name='ferias_list') ,
    url(r'^ferias/cria_ferias/$', FeriasCreate.as_view(), name='ferias_create'),
    url(r'^ferias/edita_ferias/(?P<pk>\d+)$', FeriasUpdate.as_view(), name='ferias_update'),
    url(r'^ferias/remove_ferias/(?P<pk>\d+)$', FeriasDelete.as_view(), name='ferias_delete'),
    url(r'^ferias/detalha_ferias/(?P<pk>\d+)$', FeriasDetail.as_view(), name='ferias_detail'),

    url(r'^licencas/lista_licencas/$', LicencasList.as_view(), name='licencas_list') ,
    url(r'^licencas/cria_licencas/$', LicencasCreate.as_view(), name='licencas_create'),
    url(r'^licencas/edita_licencas/(?P<pk>\d+)$', LicencasUpdate.as_view(), name='licencas_update'),
    url(r'^licencas/remove_licencas/(?P<pk>\d+)$', LicencasDelete.as_view(), name='licencas_delete'),
    url(r'^licencas/detalha_licencas/(?P<pk>\d+)$', LicencasDetail.as_view(), name='licencas_detail'),

    url(r'^lista_historico_pagamentos/$', Historico_PagamentosList.as_view(), name='historicoPagamento_list')
)
