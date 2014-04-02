from django.shortcuts import render
from estoque.models import Ingrediente, Inventario, ListaCompras, MedidaIngrediente
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

# CRUD Ingrediente
class IngredienteList(ListView):
    model = Ingrediente
    template_name = 'ingrediente/ingrediente_list.html'
    context_object_name = 'lista_ingredientes'
    success_url = reverse_lazy('ingrediente_list')

class IngredienteCreate(CreateView):
	model = Ingrediente
	template_name = 'ingrediente/ingrediente_form.html'
	fields = ['nome','marca','descricao']
	success_url = reverse_lazy('ingrediente_list')

class IngredienteUpdate(UpdateView):
	model = Ingrediente
	template_name = 'ingrediente/ingrediente_form.html'
	fields = ['nome', 'marca', 'descricao']
	success_url = reverse_lazy('ingrediente_list')

class IngredienteDelete(DeleteView):
    model = Ingrediente
    template_name = 'ingrediente/ingrediente_delete.html'
    success_url = reverse_lazy('ingrediente_list')

# CRUD MedidaIngrediente
class MedidaList(ListView):
    model = MedidaIngrediente
    template_name = 'medida/medida_list.html'
    context_object_name = 'lista_medida'
    success_url = reverse_lazy('medida_list')

class MedidaCreate(CreateView):
	model = MedidaIngrediente
	template_name = 'medida/medida_form.html'
	fields = ['ingrediente','medida']
	success_url = reverse_lazy('medida_list')

class MedidaUpdate(UpdateView):
	model = MedidaIngrediente
	template_name = 'medida/medida_form.html'
	fields = ['ingrediente', 'medida']
	success_url = reverse_lazy('medida_list')

class MedidaDelete(DeleteView):
    model = MedidaIngrediente
    template_name = 'medida/medida_delete.html'
    success_url = reverse_lazy('medida_list')


# CRUD Inventario
class InventarioList(ListView):
    model = Inventario
    template_name = 'inventario/inventario_list.html'
    context_object_name = 'lista_inventario'
    success_url = reverse_lazy('inventario_list')

class InventarioCreate(CreateView):
	model = Inventario
	template_name = 'inventario/inventario_form.html'
	fields = ['ingrediente','quantidade']
	success_url = reverse_lazy('inventario_list')

class InventarioUpdate(UpdateView):
	model = Inventario
	template_name = 'inventario/inventario_form.html'
	fields = ['ingrediente','quantidade']
	success_url = reverse_lazy('inventario_list')

class InventarioDelete(DeleteView):
    model = Inventario
    template_name = 'inventario/inventario_delete.html'
    success_url = reverse_lazy('inventario_list')

# CRUD ListaCompras
class ListaComprasList(ListView):
    model = ListaCompras
    template_name = 'listaCompras/listaCompras_list.html'
    context_object_name = 'lista_listaCompras'
    success_url = reverse_lazy('listaCompras_list')

class ListaComprasCreate(CreateView):
	model = ListaCompras
	template_name = 'listaCompras/listaCompras_form.html'
	fields = ['ingrediente','quantidade']
	success_url = reverse_lazy('listaCompras_list')
