from django.conf.urls import patterns, include, url
from tastypie.api import Api
from PCS2044.api import *
from financeiro.views import EntradaList, SaidaList, SaldoMesList, EntradaCreate, EntradaUpdate, EntradaDelete
from django.views.generic import TemplateView
from financeiro.api import *

# RESTful api
api = Api(api_name='rest')
# api.register(UserResource())
api.register(EntradaResource())

urlpatterns = patterns('',
    # root url for the financeiro app
    url(r'^$', TemplateView.as_view(template_name="../templates/index_financeiro.html"), name="index_financeiro"),
    
    # urls for models's List and CRUD views
    url(r'^entrada/lista_entrada/$', EntradaList.as_view(), name='entrada_list'),
    url(r'^entrada/cria_entrada/$', EntradaCreate.as_view(), name='entrada_create'),
    url(r'^entrada/edita_entrada/(?P<pk>\d+)$', EntradaUpdate.as_view(), name='entrada_update'),
    url(r'^entrada/remove_entrada/(?P<pk>\d+)$', EntradaDelete.as_view(), name='entrada_delete'),
    url(r'^saida/lista_saida/$', SaidaList.as_view(), name="saida_list"),
    url(r'^saldomes/lista_saldomes/$', SaldoMesList.as_view(), name="saldomes_list"),

    # url for the Financeiro's RESTfulapi
    url(r'^api/', include(api.urls)),
)