from django.conf.urls import patterns, include, url
from tastypie.api import Api
from api import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    #URLS de Entregadores
    #url(r'^entregadores/novo$','rh.views.create_funcionario'),
    #url(r'^entregadores/editar/(?P<funcionario_id>[0-9]+)/$','rh.views.edit_funcionario'),
    url(r'^entregadores/mapa/(?P<funcionario_id>[0-9]+)/$','rh.views.funcionario_detail'),
    #url(r'^entregadores/deletar/(?P<funcionario_id>[0-9]+)/$','rh.views.delete_funcionario'),
    #url(r'^entregadores/$','rh.views.index'),
    
    #url(r'^clustering/$','pedido.views.clustering'),
    #URLS paginas estaticas
    url(r'^', include('staticPages.urls', namespace="staticPages")),
    url(r'^financeiro/', include('financeiro.urls')),
    url(r'^rh/', include('rh.urls')),
    url(r'^estoque/', include('estoque.urls')),
    url(r'^cardapio/', include('cardapio.urls')),
    url(r'^promocao/', include('promocao.urls')),
    url(r'entrega/', include('entrega.urls')),
    url(r'pedido/', include('pedido.urls')),

    
    #URLS login
    #url(r'^login/(?P<data=>$)', 'login.views.login'),
    url(r'^login$', 'login.views.login'),
    url(r'^logout', 'login.views.logout'),
    # Examples:
    # url(r'^$', 'PCS2044.views.home', name='home'),
    # url(r'^PCS2044/', include('PCS2044.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^novo_pedido/','orderGrouping.views.create_order'),
)
