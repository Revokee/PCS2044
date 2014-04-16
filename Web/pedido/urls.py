from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    #URLS de pedido
    url(r'^$','pedido.views.index'),
    url(r'^index','pedido.views.index'),
    url(r'^novo$','pedido.views.novo'),
    url(r'^deletar/(?P<pedido_id>[0-9]+)/$', 'pedido.views.deletar'),
    url(r'^pagar/(?P<pedido_id>[0-9]+)/$', 'pedido.views.pagar'),
    url(r'^fechar/(?P<pedido_id>[0-9]+)/$', 'pedido.views.fechar'),
)
