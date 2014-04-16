from django.shortcuts import render
from estoque.models import Ingrediente, Inventario, ListaCompras, MedidaIngrediente
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from django.http import HttpResponse
import datetime

from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

# CRUD Ingrediente
class IngredienteList(ListView):
    model = Ingrediente
    template_name = 'ingrediente/ingrediente_list.html'
    context_object_name = 'lista_ingredientes'
    success_url = reverse_lazy('ingrediente_list')

class IngredienteCreate(SuccessMessageMixin, CreateView):
	model = Ingrediente
	template_name = 'ingrediente/ingrediente_form.html'
	fields = ['nome','marca','descricao']
	success_url = reverse_lazy('ingrediente_list')
	success_message = "Ingrediente criado com sucesso."

class IngredienteUpdate(SuccessMessageMixin, UpdateView):
	model = Ingrediente
	template_name = 'ingrediente/ingrediente_form.html'
	fields = ['nome', 'marca', 'descricao']
	success_url = reverse_lazy('ingrediente_list')
	success_message = "Ingrediente editado com sucesso."

class IngredienteDelete(SuccessMessageMixin, DeleteView):
    model = Ingrediente
    template_name = 'ingrediente/ingrediente_delete.html'
    success_url = reverse_lazy('ingrediente_list')

    def get(self, request, *args, **kwargs):
		self.object = self.get_object()
		context = self.get_context_data(object=self.object)

		messages.success(request, 'Ingrediente removido com sucesso.')
		return self.render_to_response(context)

# CRUD MedidaIngrediente
class MedidaList(ListView):
    model = MedidaIngrediente
    template_name = 'medida/medida_list.html'
    context_object_name = 'lista_medida'
    success_url = reverse_lazy('medida_list')

class MedidaCreate(SuccessMessageMixin, CreateView):
	model = MedidaIngrediente
	template_name = 'medida/medida_form.html'
	fields = ['ingrediente','medida','embalagem','descricao']
	success_url = reverse_lazy('medida_list')
	success_message = "Medida criada com sucesso."

class MedidaUpdate(SuccessMessageMixin, UpdateView):
	model = MedidaIngrediente
	template_name = 'medida/medida_form.html'
	fields = ['ingrediente', 'medida','embalagem','descricao']
	success_url = reverse_lazy('medida_list')
	success_message = "Medida editada com sucesso."

class MedidaDelete(SuccessMessageMixin, DeleteView):
    model = MedidaIngrediente
    template_name = 'medida/medida_delete.html'
    success_url = reverse_lazy('medida_list')

    def get(self, request, *args, **kwargs):
		self.object = self.get_object()
		context = self.get_context_data(object=self.object)

		messages.success(request, 'Medida removida com sucesso.')
		return self.render_to_response(context)


# CRUD Inventario
class InventarioList(ListView):
    model = Inventario
    template_name = 'inventario/inventario_list.html'
    context_object_name = 'lista_inventario'
    success_url = reverse_lazy('inventario_list')

class InventarioCreate(SuccessMessageMixin, CreateView):
	model = Inventario
	template_name = 'inventario/inventario_form.html'
	fields = ['ingrediente','quantidade']
	success_url = reverse_lazy('inventario_list')
	success_message = "Inventario criado com sucesso."

class InventarioUpdate(SuccessMessageMixin, UpdateView):
	model = Inventario
	template_name = 'inventario/inventario_form.html'
	fields = ['ingrediente','quantidade']
	success_url = reverse_lazy('inventario_list')
	success_message = "Inventario editado com sucesso."

class InventarioDelete(SuccessMessageMixin, DeleteView):
    model = Inventario
    template_name = 'inventario/inventario_delete.html'
    success_url = reverse_lazy('inventario_list')

    def get(self, request, *args, **kwargs):
		self.object = self.get_object()
		context = self.get_context_data(object=self.object)

		messages.success(request, 'Inventario removido com sucesso.')
		return self.render_to_response(context)

# CRUD ListaCompras
class ListaComprasList(ListView):
    model = ListaCompras
    template_name = 'listaCompras/listaCompras_list.html'
    context_object_name = 'lista_listaCompras'
    success_url = reverse_lazy('listaCompras_list')

class ListaComprasCreate(SuccessMessageMixin, CreateView):
	model = ListaCompras
	template_name = 'listaCompras/listaCompras_form.html'
	fields = ['ingrediente','quantidade']
	success_url = reverse_lazy('listaCompras_list')

# Custom views
def current_datetime(request):
	template_name = 'inventario/inventario_list.html'
	now = datetime.datetime.now()
	return HttpResponse()

	success_message = "Lista de Compras criada com sucesso."
