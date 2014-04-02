from django.conf.urls import patterns, include, url
from pizza5.estoque.views import IngredienteList, IngredienteCreate, IngredienteUpdate, IngredienteDelete 
from pizza5.estoque.views import InventarioList, InventarioCreate, InventarioUpdate, InventarioDelete
from pizza5.estoque.views import MedidaList, MedidaCreate, MedidaUpdate, MedidaDelete
from pizza5.estoque.views import ListaComprasList, ListaComprasCreate
from django.views.generic import TemplateView
from tastypie.api import Api
from pizza5.api import *
from pizza5.estoque.api import *

# RESTful api
api = Api(api_name='rest')
api.register(IngredienteResource())

urlpatterns = patterns('',
	# root url for the financeiro app
    url(r'^$', TemplateView.as_view(template_name="../templates/index_estoque.html"), name="index_estoque"),

	# Urls - Ingrediente
    url(r'^ingrediente/lista_ingrediente/$', IngredienteList.as_view(), name='ingrediente_list'),
    url(r'^ingrediente/cria_ingrediente/$', IngredienteCreate.as_view(), name='ingrediente_create'),
    url(r'^ingrediente/edita_ingrediente/(?P<pk>\d+)$', IngredienteUpdate.as_view(), name='ingrediente_update'),
    url(r'^ingrediente/remove_ingrediente/(?P<pk>\d+)$', IngredienteDelete.as_view(), name='ingrediente_delete'),

    # Urls - Medidas
    url(r'^medida/lista_medida/$', MedidaList.as_view(), name='medida_list'),
    url(r'^medida/cria_medida/$', MedidaCreate.as_view(), name='medida_create'),
    url(r'^medida/edita_medida/(?P<pk>\d+)$', MedidaUpdate.as_view(), name='medida_update'),
    url(r'^medida/remove_medida/(?P<pk>\d+)$', MedidaDelete.as_view(), name='medida_delete'),

    # Urls - Inventario
    url(r'^inventario/lista_inventario/$', InventarioList.as_view(), name='inventario_list'),
    url(r'^inventario/cria_inventario/$', InventarioCreate.as_view(), name='inventario_create'),
    url(r'^inventario/edita_inventario/(?P<pk>\d+)$', InventarioUpdate.as_view(), name='inventario_update'),
    url(r'^inventario/remove_inventario/(?P<pk>\d+)$', InventarioDelete.as_view(), name='inventario_delete'),

    # Urls - ListaCompras
    url(r'^listaCompras/lista_listaCompras/$', ListaComprasList.as_view(), name='listaCompras_list'),
    url(r'^listaCompras/cria_listaCompras/$', ListaComprasCreate.as_view(), name='listaCompras_create'),
    # url(r'^inventario/edita_inventario/(?P<pk>\d+)$', InventarioUpdate.as_view(), name='inventario_update'),
    # url(r'^inventario/remove_inventario/(?P<pk>\d+)$', InventarioDelete.as_view(), name='inventario_delete')

    # APIs - Inventario
    url(r'^api/', include(api.urls))
)
