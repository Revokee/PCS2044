from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    #URLS de Entregadores
    url(r'^entregadores/novo$','rh.views.create_funcionario'),
    url(r'^entregadores/editar/(?P<entregador_id>[0-9]+)/$','rh.views.edit_funcionario'),
    url(r'^entregadores/mapa/(?P<entregador_id>[0-9]+)/$','rh.views.funcionario_detail'),
    url(r'^entregadores/deletar/(?P<entregador_id>[0-9]+)/$','rh.views.delete_funcionario'),
    url(r'^entregadores/$','rh.views.index'),
    
    #URLS de Pedidos
    url(r'^pedidos/novo$','pedido.views.create_pedido'),
    url(r'^pedidos/$','pedido.views.index'),
    url(r'^deletar_pedido/(?P<order_id>[0-9]+)/$', 'pedido.views.delete_pedido'),
    url(r'^', include('staticPages.urls', namespace="staticPages")),
    #url(r'', 'staticPages.views.home'),
    # Examples:
    # url(r'^$', 'PCS2044.views.home', name='home'),
    # url(r'^PCS2044/', include('PCS2044.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^novo_pedido/','orderGrouping.views.create_order'),
)
