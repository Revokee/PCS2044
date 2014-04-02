from django.conf.urls import patterns, include, url
from tastypie.api import Api
from pizza5.api import *
from pizza5.financeiro.views import *
from django.views.generic import TemplateView
from pizza5.financeiro.api import *

# RESTful api
api = Api(api_name='rest')
api.register(FormaPagamentoResource())
api.register(EntradaResource())
api.register(SaidaResource())

urlpatterns = patterns('',
    # root url for the financeiro app
    #url(r'^$', TemplateView.as_view(template_name="../templates/index_financeiro.html"), name="index_financeiro"),
    url(r'^$', IndexInteligente, name="index_financeiro"),
    # urls for models's List and CRUD views
    
    url(r'^entrada/$', EntradaList.as_view(), name='entrada_list'),
    url(r'^entrada/cria_entrada/$', EntradaCreate.as_view(), name='entrada_create'),
    url(r'^entrada/edita_entrada/(?P<pk>\d+)$', EntradaUpdate.as_view(), name='entrada_update'),
    url(r'^entrada/remove_entrada/(?P<pk>\d+)$', EntradaDelete.as_view(), name='entrada_delete'),
    url(r'^entrada/detalha_entrada/(?P<pk>\d+)$', EntradaDetail.as_view(), name='entrada_detail'),
    
    url(r'^saida/$', SaidaList.as_view(), name="saida_list"),
    url(r'^saida/cria_saida/$', SaidaCreate.as_view(), name='saida_create'),
    url(r'^saida/edita_saida/(?P<pk>\d+)$', SaidaUpdate.as_view(), name='saida_update'),
    url(r'^saida/remove_saida/(?P<pk>\d+)$', SaidaDelete.as_view(), name='saida_delete'),
    url(r'^saida/detalha_saida/(?P<pk>\d+)$', SaidaDetail.as_view(), name='saida_detail'),
    
    url(r'^saldomes/lista_saldomes/$', SaldoMesList.as_view(), name="saldomes_list"),

    # url for the Financeiro's RESTfulapi
    url(r'^api/', include(api.urls)),
)
