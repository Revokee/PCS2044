from django.conf.urls import patterns, include, url
from tastypie.api import Api
from api import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    #URLS de Entregadores
    url(r'^funcionarios/novo$','rh.views.create_funcionario'),
    url(r'^funcionarios/editar/(?P<funcionario_id>[0-9]+)/$','rh.views.edit_funcionario'),
    url(r'^funcionarios/mapa/(?P<funcionario_id>[0-9]+)/$','rh.views.funcionario_detail'),
    url(r'^funcionarios/deletar/(?P<funcionario_id>[0-9]+)/$','rh.views.delete_funcionario'),
    url(r'^funcionarios/$','rh.views.index'),
    
    #URLS de Pedidos
    url(r'^pedidos/novo$','pedido.views.create_pedido'),
    url(r'^pedidos.json$','pedido.json.pedidos'),
    url(r'^pedidos','pedido.views.index'),
    url(r'^deletar_pedido/(?P<pedido_id>[0-9]+)/$', 'pedido.views.delete_pedido'),
    url(r'^pagar_pedido/(?P<pedido_id>[0-9]+)/$', 'pedido.views.pagar_pedido'),
    url(r'^fechar_pedido/(?P<pedido_id>[0-9]+)/$', 'pedido.views.fechar_pedido'),
    url(r'^planejamento/$','pedido.views.planejamento'),
    #URLS paginas estaticas
    url(r'^', include('staticPages.urls', namespace="staticPages")),
    url(r'^financeiro/', include('financeiro.urls')),
    url(r'^rh/', include('rh.urls')),
    
    #URLS login
    url(r'^login', 'login.views.login'),
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
